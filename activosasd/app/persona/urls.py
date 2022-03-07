from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet

router = DefaultRouter()

router.register(r'',PersonaViewSet,basename = 'personas_all')

urlpatterns = router.urls