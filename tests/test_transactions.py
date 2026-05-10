import pytest
from datetime import datetime

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

from transactions.models import (
    Tickets,
    TicketsDetails
)

from services.models import (
    Areas,
    Sedes,
    AreasSedes,
    Categories
)

from authentication.models import (
    UsersSedes
)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def setup_data():

    area = Areas.objects.create(
        name='Sistemas',
        is_active=True
    )

    sede = Sedes.objects.create(
        name='Lima',
        is_active=True
    )

    area_sede = AreasSedes.objects.create(
        area=area,
        sede=sede,
        is_active=True
    )

    category = Categories.objects.create(
        name='Soporte TI',
        is_active=True
    )

    return {
        'area': area,
        'sede': sede,
        'area_sede': area_sede,
        'category': category
    }


@pytest.fixture
def auth_user():

    user = User.objects.create_user(
        username='admin',
        password='123456'
    )

    return user


@pytest.mark.django_db
class TestTickets:

    def test_create_ticket_success(
        self,
        api_client,
        setup_data
    ):

        payload = {
            'ticket_detail': {
                'applicant': 'Juan Perez',
                'email': 'juan@test.com',
                'phone': '999888777',
                'description': 'No funciona el sistema',
                'area_sede': setup_data['area_sede'].id,
                'category': setup_data['category'].id
            }
        }

        response = api_client.post(
            '/api/tickets/',
            payload,
            format='json'
        )

        assert response.status_code == status.HTTP_201_CREATED

        assert Tickets.objects.count() == 1

        ticket = Tickets.objects.first()

        assert ticket.code is not None

        assert ticket.access_key is not None

        assert ticket.status == 'REGISTRADO'

        assert ticket.ticket_detail.applicant == 'Juan Perez'


    def test_create_ticket_generates_code(
        self,
        api_client,
        setup_data
    ):

        payload = {
            'ticket_detail': {
                'applicant': 'Juan Perez',
                'email': 'juan@test.com',
                'phone': '999888777',
                'description': 'Error sistema',
                'area_sede': setup_data['area_sede'].id,
                'category': setup_data['category'].id
            }
        }

        response = api_client.post(
            '/api/tickets/',
            payload,
            format='json'
        )

        assert response.status_code == status.HTTP_201_CREATED

        ticket = Tickets.objects.first()

        year = datetime.now().year

        assert ticket.code == f'T-000001-{year}'


    def test_create_ticket_without_email(
        self,
        api_client,
        setup_data
    ):

        payload = {
            'ticket_detail': {
                'applicant': 'Juan Perez',
                'phone': '999888777',
                'description': 'Error sistema',
                'area_sede': setup_data['area_sede'].id,
                'category': setup_data['category'].id
            }
        }

        response = api_client.post(
            '/api/tickets/',
            payload,
            format='json'
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert Tickets.objects.count() == 0


    def test_list_tickets_requires_authentication(
        self,
        api_client
    ):

        response = api_client.get('/api/tickets/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_list_tickets_authenticated_user(
        self,
        api_client,
        auth_user,
        setup_data
    ):

        UsersSedes.objects.create(
            user=auth_user,
            sede=setup_data['sede'],
            is_active=True
        )

        ticket_detail = TicketsDetails.objects.create(
            applicant='Juan',
            email='juan@test.com',
            phone='999999999',
            description='Error sistema',
            area_sede=setup_data['area_sede'],
            category=setup_data['category']
        )

        Tickets.objects.create(
            ticket_detail=ticket_detail,
            code='T-000001-2026',
            access_key='ABC123',
            status='REGISTRADO'
        )

        api_client.force_authenticate(user=auth_user)

        response = api_client.get('/api/tickets/')

        assert response.status_code == status.HTTP_200_OK

        assert len(response.data) == 1


    def test_user_only_sees_his_sede_tickets(
        self,
        api_client,
        auth_user
    ):

        area = Areas.objects.create(
            name='Sistemas',
            is_active=True
        )

        sede_lima = Sedes.objects.create(
            name='Lima',
            is_active=True
        )

        sede_ica = Sedes.objects.create(
            name='Ica',
            is_active=True
        )

        area_sede_lima = AreasSedes.objects.create(
            area=area,
            sede=sede_lima,
            is_active=True
        )

        area_sede_ica = AreasSedes.objects.create(
            area=area,
            sede=sede_ica,
            is_active=True
        )

        category = Categories.objects.create(
            name='Soporte',
            is_active=True
        )

        UsersSedes.objects.create(
            user=auth_user,
            sede=sede_lima,
            is_active=True
        )

        ticket_detail_lima = TicketsDetails.objects.create(
            applicant='Juan',
            email='juan@test.com',
            phone='999999999',
            description='Ticket Lima',
            area_sede=area_sede_lima,
            category=category
        )

        ticket_detail_ica = TicketsDetails.objects.create(
            applicant='Pedro',
            email='pedro@test.com',
            phone='999999998',
            description='Ticket Ica',
            area_sede=area_sede_ica,
            category=category
        )

        Tickets.objects.create(
            ticket_detail=ticket_detail_lima,
            code='T-000001-2026',
            access_key='AAA111',
            status='REGISTRADO'
        )

        Tickets.objects.create(
            ticket_detail=ticket_detail_ica,
            code='T-000002-2026',
            access_key='BBB222',
            status='REGISTRADO'
        )

        api_client.force_authenticate(user=auth_user)

        response = api_client.get('/api/tickets/')

        assert response.status_code == status.HTTP_200_OK

        assert len(response.data) == 1

        assert (
            response.data[0]['ticket_detail']['description']
            == 'Ticket Lima'
        )