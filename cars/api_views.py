from django.db.models import Count
from rest_framework import (
    viewsets,
    status
)
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from cars.models import Car
from cars.serializers import CarSerializer
from common.external_api import ExternalApiConnector


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all().order_by('id')
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        connector = ExternalApiConnector(make=str(self.request.POST.get('make')).lower(),
                                         vehicle_model=str(self.request.POST.get('model')).lower())

        if connector.check_model_for_make() is not bool:
            status_code = connector.check_model_for_make()
            return Response(status=status_code, data={'message': f'External API responded with a status of {status_code}'})

        elif connector.check_model_for_make():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Not found'})

    def retrieve(self, request, *args, **kwargs):
        response = {'detail': 'Retrieve not allowed.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class CarSortedBydPopularityListApiView(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.annotate(count=Count('rate')).order_by('-count')
