from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class TicketsDetails(models.Model):
    applicant = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    description = models.TextField()
    area_sede = models.ForeignKey(
        'services.AreasSedes',
        on_delete=models.CASCADE,
        db_column = 'area_sede_id',
        related_name='tickets_details'
    )
    category = models.ForeignKey(
        'services.Categories',
        on_delete=models.CASCADE,
        db_column = 'category_id',
        related_name='tickets_details'
    )

class Tickets(models.Model):
    TICKET_STATUS = (
        ('REGISTRADO', 'Registrado'),
        ('ASIGNADO', 'Asignado'),
        ('ATENDIDO', 'Atendido'),
        ('CERRADO', 'Cerrado'),
    )
    ticket_detail = models.OneToOneField(
        TicketsDetails,
        on_delete=models.CASCADE,
        db_column = 'ticket_detail_id',
        related_name='tickets'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column = 'user_id',
        related_name='tickets',
        null=True,
        blank=True
    )
    code = models.CharField(max_length=15, unique=True)
    access_key = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=TICKET_STATUS, default='REGISTRADO')
    date_assigned = models.DateTimeField(blank=True, null=True)
    date_attention = models.DateTimeField(blank=True, null=True)
    solution = models.TextField(blank=True)
    valoration = models.IntegerField(
        blank=True, 
        null=True, 
        validators=[
            MinValueValidator(1), MaxValueValidator(5)
        ]
    )
    date_closed = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

