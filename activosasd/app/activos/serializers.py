from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer, CharField, DateTimeField


from .models import Activos, TipoActivo
from ..area.models import Area
from ..persona.models import Persona
from ..persona.serializers import PersonaSerializer


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

class CreateActivoSerializer(Serializer):
    """
    Validación de la data recibida

    """
    nombre = CharField(max_length=50, required=True)
    descripcion = CharField(max_length=250)
    serial = CharField(max_length=250, required=True)
    numerointerno = CharField(max_length=250, required=True)
    peso = CharField(max_length=250, required=True)
    alto = CharField(max_length=250, required=True)
    ancho = CharField(max_length=250, required=True)
    largo = CharField(max_length=250, required=True)
    valorcompra = CharField(max_length=250, required=True)
    fechacompra = DateTimeField(required=True)
    fechabaja = DateTimeField(allow_null=True)
    color = CharField(max_length=250, required=True)
    area = CharField(max_length=250, required=True)
    persona = CharField(max_length=250, required=True)
    tipo_activo = CharField(max_length=250, required=True)


    def create(self, data):
        try:
            area_exist = Area.objects.get(nombre=data.get('area'))
        except Area.DoesNotExist:
            raise ValidationError({"area": ['No existe esa area']})
        try:
            persona_exist = Persona.objects.get(primernombre=data.get('persona'))
        except Persona.DoesNotExist:
            raise ValidationError({"persona": ['No existe esta persona']})
        try:
            tipo_exist = TipoActivo.objects.get(nombre=data.get('tipo_activo'))
        except TipoActivo.DoesNotExist:
            raise ValidationError({"tipo activo": ['El tipo de activo no existe']})

        activos = Activos(
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion'),
            serial=data.get('serial'),
            numerointerno=data.get('numerointerno'),
            peso=data.get('peso'),
            alto=data.get('alto'),
            ancho=data.get('ancho'),
            largo=data.get('largo'),
            valorcompra=data.get('valorcompra'),
            fechacompra=data.get('fechacompra'),
            estadoactual=data.get('estadoactual'),
            color=data.get('color'),
            area=Area.objects.get(id=area_exist.id),
            persona=Persona.objects.get(id=persona_exist.id),
            tipo=TipoActivo.objects.get(id=tipo_exist.id)
        )
        activos.save()
        return data