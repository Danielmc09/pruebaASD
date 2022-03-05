from django.db import models

# Create your models here.
from app.ubicacion.models import Ciudad


class Area(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'area'
