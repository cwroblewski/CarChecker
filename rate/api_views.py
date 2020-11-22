from rest_framework import (
    viewsets,
    status
)
from rest_framework.response import Response

from rate.serializers import RateSerializer
from rate.models import Rate


class RateViewSet(viewsets.ModelViewSet):

    serializer_class = RateSerializer
    queryset = Rate.objects.all()
    http_method_names = ['get', 'post']

    def retrieve(self, request, *args, **kwargs):
        response = {'detail': 'Retrieve not allowed.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)
