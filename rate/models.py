from django.db import models

from cars.models import Car
from common.models import Registry


RATES_CHOICES = [
    (1, 'Very bad'),
    (2, 'Bad'),
    (3, 'Ok'),
    (4, 'Good'),
    (5, 'Very good'),
]


class Rate(Registry):
    """Rate model."""

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rate = models.IntegerField(verbose_name='users rate', choices=RATES_CHOICES)

    def __str__(self):
        return f'Car: {self.car}, rate: {self.rate}'
