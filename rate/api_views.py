from rest_framework import viewsets
from rate.serializers import RateSerializer
from rate.models import Rate


class RateViewSet(viewsets.ModelViewSet):

    serializer_class = RateSerializer
    queryset = Rate.objects.all()
