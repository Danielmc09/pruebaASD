from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (ActivoViewSet)

urlpatterns = [
    path('', ActivoViewSet.as_view(), name='list_all_services'),
]