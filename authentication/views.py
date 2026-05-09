from django.shortcuts import render
from rest_framework import generics
from .models import (
    Roles,
    UsersRoles,
    UsersSedes
)
from .serializers import (
    RoleSerializer,
    UserSerializer,
    UserRoleSerializer,
    UserSedeSerializer
)
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Usuarios'])
class RolesView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['Usuarios'])
class ManageRolesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['Usuarios'])
class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['Usuarios'])
class ManageUsersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

@extend_schema(tags=['Usuarios'])
class UsersRolesView(generics.ListCreateAPIView):
    queryset = UsersRoles.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(tags=['Usuarios'])
class UsersSedesView(generics.ListCreateAPIView):
    queryset = UsersSedes.objects.all()
    serializer_class = UserSedeSerializer
    permission_classes = [IsAuthenticated]