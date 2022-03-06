from datetime import datetime, date

from rest_framework import generics, status
from rest_framework.response import Response

from .models import Activos, TipoActivo
from .querys import query_for_tipo, query_for_fechacompra, query_for_serial
from .serializers import ActivoSerializer


class ActivoViewSet(generics.ListAPIView):
    serializer_class = ActivoSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()


class ListActivosTipoViewSet(generics.ListAPIView):

    def get(self, request):
        tipo_activo = self.request.GET.get('tipo_activo')
        tipoactivo_exist = TipoActivo.objects.filter(nombre=tipo_activo)
        if tipo_activo != '' and len(tipoactivo_exist) != 0:
            get_queryset = query_for_tipo(tipo_activo)
            queryset = {
                'activos_asosiados_al_tipo': get_queryset
            }
            return Response(data=queryset, status=status.HTTP_200_OK)
        else:
            queryset = {
                'activos_asosiados_al_tipo': 'Busqueda sin resultados'
            }
            return Response(data=queryset, status=status.HTTP_404_NOT_FOUND)


class ListActivosFechaCompraViewSet(generics.ListAPIView):

    def get(self, request):
        fecha_compra = self.request.GET.get('fecha_compra')
        fecha_compra = fecha_compra if fecha_compra != '' else '0001-01-01'
        fecha_compra = datetime.strptime(fecha_compra, '%Y-%m-%d')
        fechacompra_exist = Activos.objects.filter(
            fechacompra__date=date(int(fecha_compra.year), int(fecha_compra.month), int(fecha_compra.day)))
        if fecha_compra != '' and len(fechacompra_exist) != 0:
            get_queryset = query_for_fechacompra(fecha_compra)
            queryset = {
                'activos_asosiados_a_fecha_compra': get_queryset
            }
            return Response(data=queryset, status=status.HTTP_200_OK)
        else:
            queryset = {
                'activos_asosiados_a_fecha_compra': 'Busqueda sin resultados'
            }
            return Response(data=queryset, status=status.HTTP_404_NOT_FOUND)


class ListActivosSerialViewSet(generics.ListAPIView):

    def get(self, request):
        serial = self.request.GET.get('serial')
        serial_exist = Activos.objects.filter(serial=serial)
        if serial != '' and len(serial_exist) != 0:
            get_queryset = query_for_serial(serial)
            queryset = {
                'activos_asosiados_a_el_serial': get_queryset
            }
            return Response(data=queryset, status=status.HTTP_200_OK)
        else:
            queryset = {
                'activos_asosiados_a_el_serial': 'Busqueda sin resultados'
            }
            return Response(data=queryset, status=status.HTTP_404_NOT_FOUND)

