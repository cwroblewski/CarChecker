from rest_framework import serializers

from cars.models import (
    Car,
    Rate
)


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ('rate', )


class CarSerializer(serializers.ModelSerializer):
    rate_set = RatingSerializer(many=True)

    class Meta:
        model = Car
        fields = ('make', 'model', 'rate_set')
