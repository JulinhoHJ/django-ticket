from rest_framework import serializers
from .models import (
    TicketsDetails,
    Tickets
)
import secrets
import string
from datetime import datetime
from django.db import transaction

class TicketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsDetails
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    ticket_detail = TicketDetailSerializer()
    class Meta:
        model = Tickets
        fields = (
            'ticket_detail',
            'code',
            'access_key',
            'status'
        )
        read_only_fields = (
            'code',
            'access_key',
            'status'
        )

    def generate_access_key(self, length=6):

        characters = string.ascii_uppercase + string.digits

        return ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

    @transaction.atomic
    def create(self, validated_data):
        ticket_detail_data = validated_data.pop('ticket_detail')
        ticket_detail_instance = TicketsDetails.objects.create(
            **ticket_detail_data
        )

        year = datetime.now().year
        last_ticket = Tickets.objects.filter(
            code__endswith=str(year)
        ).order_by('-id').first()

        new_number = 1
        if last_ticket:
            last_number = int(
                last_ticket.code.split('-')[1]
            )
            new_number = last_number + 1

        new_code = f'T-{str(new_number).zfill(6)}-{year}'
        access_key = self.generate_access_key()

        ticket_instance = Tickets.objects.create(
            ticket_detail=ticket_detail_instance,
            code=new_code,
            access_key=access_key,
            status='REGISTRADO',
            **validated_data
        )
        return ticket_instance