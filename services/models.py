from django.db import models

class Areas(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Sedes(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class AreasSedes(models.Model):
    area = models.ForeignKey(
        Areas,
        on_delete=models.CASCADE,
        db_column = 'area_id',
        related_name='areas_sedes'
    )
    sede = models.ForeignKey(
        Sedes,
        on_delete=models.CASCADE,
        db_column = 'sede_id',
        related_name='areas_sedes'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Categories(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
