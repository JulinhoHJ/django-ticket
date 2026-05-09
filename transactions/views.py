from django.shortcuts import render
from rest_framework import generics
from .models import (
    Tickets
)
from .serializers import (
    TicketSerializer
)
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Transacciones'])
class TicketsView(generics.ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer