from rest_framework import serializers
from .models import Activos, TipoActivo


class TipoActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoActivo
        exclude = ['created', 'update']

class ActivoSerializer(serializers.ModelSerializer):
    tipo = serializers.StringRelatedField()
    area = serializers.StringRelatedField()
    persona = serializers.StringRelatedField()

    class Meta:
        model = Activos
        exclude = ['created', 'update']
