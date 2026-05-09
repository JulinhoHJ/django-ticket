from django.shortcuts import render

from rest_framework import generics
from .models import (
    Areas,
    Sedes,
    AreasSedes,
    Categories
)
from .serializers import (
    AreaSerializer,
    SedeSerializer,
    AreaSedeSerializer,
    CategorySerializer
)
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from datetime import datetime
from rest_framework.permissions import IsAuthenticated

@extend_schema(tags=['Servicios'])
class AreasView(generics.ListCreateAPIView):
    queryset = Areas.objects.filter(is_active=True)
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['Servicios'])
class ManageAreasView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Areas.objects.filter(is_active=True)
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

@extend_schema(tags=['Servicios'])
class SedesView(generics.ListCreateAPIView):
    queryset = Sedes.objects.filter(is_active=True)
    serializer_class = SedeSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['Servicios'])
class ManageSedesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sedes.objects.filter(is_active=True)
    serializer_class = SedeSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

@extend_schema(tags=['Servicios'])
class AreasSedesView(generics.ListCreateAPIView):
    queryset = AreasSedes.objects.filter(is_active=True)
    serializer_class = AreaSedeSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['Servicios'])
class ManageAreasSedesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AreasSedes.objects.filter(is_active=True)
    serializer_class = AreaSedeSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

@extend_schema(tags=['Servicios'])
class CategoriesView(generics.ListCreateAPIView):
    queryset = Categories.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['Servicios'])
class ManageCategoriesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()