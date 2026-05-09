from django.shortcuts import render
from rest_framework import generics
from .models import (
    Tickets
)
from .serializers import (
    TicketSerializer
)
from authentication.models import (
    UsersSedes
)
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)

@extend_schema(tags=['Transacciones'])
class TicketsView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Tickets.objects.all()

        user_sedes = UsersSedes.objects.filter(
            user=user,
            is_active=True
        ).values_list(
            'sede_id',
            flat=True
        )

        return Tickets.objects.filter(
            ticket_detail__area_sede__sede_id__in=user_sedes
        )