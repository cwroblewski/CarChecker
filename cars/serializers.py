from django.db.models import Avg
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):

    rates_no = serializers.SerializerMethodField()
    average_rate = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ('make', 'model', 'rates_no', 'average_rate', )

        validators = [
            UniqueTogetherValidator(
                queryset=Car.objects.all(),
                fields=['make', 'model']
            )
        ]

    def get_rates_no(self, obj):
        return obj.rate_set.all().count()

    def get_average_rate(self, obj):
        return obj.rate_set.aggregate(Avg('rate'))['rate__avg']
