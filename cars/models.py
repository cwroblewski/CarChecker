from django.db import models

from common.models import Registry


class Car(Registry):
    """Car model."""

    make = models.CharField(verbose_name='marka', max_length=64)
    model = models.CharField(verbose_name='model', max_length=64)

    def __str__(self):
        return f'Marka: {self.make}, model: {self.model}'
