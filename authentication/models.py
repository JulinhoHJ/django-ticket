from django.db import models
from django.contrib.auth.models import User

class Roles(models.Model):
    ROLES = (
        ('ADMINISTRADOR', 'Administrador'),
        ('SOPORTE', 'Soporte'),
    )
    name = models.CharField(max_length=20, choices=ROLES, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class UsersRoles(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column = 'user_id',
        related_name='users_roles'
    )
    role = models.ForeignKey(
        Roles,
        on_delete=models.CASCADE,
        db_column = 'role_id',
        related_name='users_roles'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class UsersSedes(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column = 'user_id',
        related_name='users_sedes'
    )
    sede = models.ForeignKey(
        'services.Sedes',
        on_delete=models.CASCADE,
        db_column = 'sede_id',
        related_name='users_sedes'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)