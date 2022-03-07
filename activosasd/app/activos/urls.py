from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (ActivoListViewSet, ListActivosTipoViewSet, ListActivosFechaCompraViewSet, ListActivosSerialViewSet,
                    ActivoCreateViewSet)

urlpatterns = [
    path('', ActivoListViewSet.as_view(), name='list_all_activos'),
    path('activoscreate/', ActivoCreateViewSet.as_view(), name='create_activos'),
    path('activostipo/', ListActivosTipoViewSet.as_view(), name='list_activos_tipo'),
    path('activosfechacompra/', ListActivosFechaCompraViewSet.as_view(), name='list_activos_fechacompra'),
    path('activosserial/', ListActivosSerialViewSet.as_view(), name='list_activos_serial'),
]