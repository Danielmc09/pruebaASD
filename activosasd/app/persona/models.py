from django.db import models


# Create your models here.


class Persona(models.Model):
    primernombre = models.CharField(max_length=50, blank=True, null=True)
    segundonombre = models.CharField(max_length=50, blank=True, null=True)
    primerapellido = models.CharField(max_length=50, blank=True, null=True)
    segundoapellido = models.CharField(max_length=50, blank=True, null=True)
    tipodocumento = models.CharField(max_length=50, blank=True, null=True)
    numerodocumento = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.primernombre

    class Meta:
        db_table = 'persona'