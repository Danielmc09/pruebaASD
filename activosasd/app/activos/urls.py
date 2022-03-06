from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (ActivoViewSet, ListActivosTipoViewSet, ListActivosFechaCompraViewSet, ListActivosSerialViewSet)

urlpatterns = [
    path('', ActivoViewSet.as_view(), name='list_all_services'),
    path('activostipo/', ListActivosTipoViewSet.as_view(), name='list_activos_tipo'),
    path('activosfechacompra/', ListActivosFechaCompraViewSet.as_view(), name='list_activos_fechacompra'),
    path('activosserial/', ListActivosSerialViewSet.as_view(), name='list_activos_serial'),
]