from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


from .serializers import AreaSerializer


class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        area_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(area_serializer.data, status=status.HTTP_200_OK)
