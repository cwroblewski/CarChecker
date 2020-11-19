from django.db.models import Count
from rest_framework import viewsets
from cars.serializers import CarSerializer
from cars.models import Car


class CarViewSet(viewsets.ModelViewSet):

    serializer_class = CarSerializer
    queryset = Car.objects.annotate(count=Count('rate')).order_by('-count')
