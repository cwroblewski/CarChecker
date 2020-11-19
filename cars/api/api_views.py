from rest_framework import viewsets
from .serializers import CarSerializer
from ..models import Car


class CarViewSet(viewsets.ModelViewSet):

    serializer_class = CarSerializer
    queryset = Car.objects.all()
