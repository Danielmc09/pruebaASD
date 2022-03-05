from django.db import models

# Create your models here.
from app.area.models import Area
from app.persona.models import Persona

CHOICE_ESTADO = [
    ('activo', 'activo'),
    ('dado de baja', 'dado de baja'),
    ('en reparación', 'en reparación'),
    ('disponible', 'disponible'),
    ('asignado', 'asignado'),
    ]

class TipoActivo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipoactivo'

class Activos(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    tipo = models.ForeignKey(TipoActivo, on_delete=models.CASCADE)
    serial = models.CharField(max_length=250, blank=True, null=True)
    numerointerno = models.CharField(max_length=250, blank=True, null=True)
    peso = models.CharField(max_length=250, blank=True, null=True)
    alto = models.CharField(max_length=250, blank=True, null=True)
    ancho = models.CharField(max_length=250, blank=True, null=True)
    largo = models.CharField(max_length=250, blank=True, null=True)
    valorcompra = models.CharField(max_length=250, blank=True, null=True)
    fechacompra = models.CharField(max_length=250, blank=True, null=True)
    fechabaja = models.CharField(max_length=250, blank=True, null=True)
    estadoactual = models.CharField(choices=CHOICE_ESTADO, max_length=20, blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    color = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'activo'