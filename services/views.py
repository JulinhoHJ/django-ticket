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
    queryset = Areas.objects.all()
    serializer_class = AreaSerializer
    #permission_classes = [IsAuthenticated]

@extend_schema(tags=['Servicios'])
class ManageAreasView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Areas.objects.all()
    serializer_class = AreaSerializer

@extend_schema(tags=['Servicios'])
class SedesView(generics.ListCreateAPIView):
    queryset = Sedes.objects.all()
    serializer_class = SedeSerializer

@extend_schema(tags=['Servicios'])
class ManageSedesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sedes.objects.all()
    serializer_class = SedeSerializer

@extend_schema(tags=['Servicios'])
class AreasSedesView(generics.ListCreateAPIView):
    queryset = AreasSedes.objects.all()
    serializer_class = AreaSedeSerializer

@extend_schema(tags=['Servicios'])
class ManageAreasSedesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AreasSedes.objects.all()
    serializer_class = AreaSedeSerializer

@extend_schema(tags=['Servicios'])
class CategoriesView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

@extend_schema(tags=['Servicios'])
class ManageCategoriesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer