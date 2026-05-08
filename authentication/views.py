from django.shortcuts import render
from rest_framework import generics
from .models import (
    Roles,
    UsersRoles
)
from .serializers import (
    RoleSerializer,
    UserSerializer,
    UserRoleSerializer
)
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Usuarios'])
class RolesView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer

@extend_schema(tags=['Usuarios'])
class ManageRolesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer

@extend_schema(tags=['Usuarios'])
class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@extend_schema(tags=['Usuarios'])
class ManageUsersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@extend_schema(tags=['Usuarios'])
class UsersRolesView(generics.ListCreateAPIView):
    queryset = UsersRoles.objects.all()
    serializer_class = UserRoleSerializer
