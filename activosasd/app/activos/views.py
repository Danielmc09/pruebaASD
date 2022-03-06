from rest_framework import generics

from .serializers import ActivoSerializer

class ActivoViewSet(generics.ListAPIView):
    serializer_class = ActivoSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()