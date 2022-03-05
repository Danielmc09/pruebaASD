from rest_framework.routers import DefaultRouter
from .views import AreaViewSet

router = DefaultRouter()

router.register(r'',AreaViewSet,basename = 'areas_all')

urlpatterns = router.urls