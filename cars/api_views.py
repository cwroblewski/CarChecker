from django.db.models import Count
from rest_framework import (
    viewsets,
    status
)
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from cars.serializers import CarSerializer
from cars.models import Car
from common.external_api import ExternalApiConnector


class CarViewSet(viewsets.ModelViewSet):

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        connector = ExternalApiConnector(make=self.request.POST.get('make'), model=self.request.POST.get('model'))

        if connector.check_in_api_db():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Not found'})


class CarSortedBydPopularityView(ListAPIView):

    serializer_class = CarSerializer
    queryset = Car.objects.annotate(count=Count('rate')).order_by('-count')
