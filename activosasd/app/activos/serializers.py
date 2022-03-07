from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer, CharField, DateTimeField

from .models import Activos, TipoActivo
from ..area.models import Area
from ..persona.models import Persona


class TipoActivoSerializer(serializers.ModelSerializer):
    """
    Serializador del modelo TipoActivo
    """

    class Meta:
        model = TipoActivo
        exclude = ['created', 'update']


class ActivoSerializer(serializers.ModelSerializer):
    """
    Serializador del modelo Activos
    """
    tipo = serializers.StringRelatedField()
    area = serializers.StringRelatedField()
    persona = serializers.StringRelatedField()

    class Meta:
        model = Activos
        exclude = ['created', 'update']


class CreateActivoSerializer(Serializer):
    """
    Validación de la data recibida para crear
    un activo

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
        fecha_compra = data.get('fechacompra')
        fecha_baja = data.get('fechabaja')
        """ Validación de fecha de baja """
        if fecha_baja is not None:
            if str(fecha_baja) > str(fecha_compra):
                raise ValidationError({"Fechabaja": ['La fecha de baja no puede ser mayor a la fecha de compra']})
            else:
                pass
        """ Validación de la existencia de las llaves foraneas """
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


class UpdateActivoSerializer(Serializer):
    """
    Validación de la data recibida para actualizar
    un activo

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

    def update(self, instance, validated_data):
        fecha_compra = validated_data.get('fechacompra')
        fecha_baja = validated_data.get('fechabaja')
        """ Validación de fecha de baja """
        if fecha_baja is not None:
            if str(fecha_baja) > str(fecha_compra):
                raise ValidationError({"Fechabaja": ['La fecha de baja no puede ser mayor a la fecha de compra']})
            else:
                pass
        """ Validación de la existencia de las llaves foraneas """
        try:
            area_exist = Area.objects.get(nombre=validated_data.get('area'))
        except Area.DoesNotExist:
            raise ValidationError({"area": ['No existe esa area']})
        try:
            persona_exist = Persona.objects.get(primernombre=validated_data.get('persona'))
        except Persona.DoesNotExist:
            raise ValidationError({"persona": ['No existe esta persona']})
        try:
            tipo_exist = TipoActivo.objects.get(nombre=validated_data.get('tipo_activo'))
        except TipoActivo.DoesNotExist:
            raise ValidationError({"tipo activo": ['El tipo de activo no existe']})

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.serial = validated_data.get('serial', instance.serial)
        instance.numerointerno = validated_data.get('numerointerno', instance.numerointerno)
        instance.peso = validated_data.get('peso', instance.peso)
        instance.alto = validated_data.get('alto', instance.alto)
        instance.ancho = validated_data.get('ancho', instance.ancho)
        instance.largo = validated_data.get('largo', instance.largo)
        instance.valorcompra = validated_data.get('valorcompra', instance.valorcompra)
        instance.fechacompra = validated_data.get('fechacompra', instance.fechacompra)
        instance.fechabaja = validated_data.get('fechabaja', instance.fechabaja)
        instance.color = validated_data.get('color', instance.color)
        instance.area = validated_data.get(Area.objects.get(id=area_exist.id), instance.area)
        instance.persona = validated_data.get(Persona.objects.get(id=persona_exist.id), instance.persona)
        instance.tipo = validated_data.get(TipoActivo.objects.get(id=tipo_exist.id), instance.tipo)
        instance.save()
        return instance