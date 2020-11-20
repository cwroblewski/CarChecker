from django.db import models

from common.models import Registry


class Car(Registry):
    """Car model."""

    make = models.CharField(verbose_name='make', max_length=64)
    model = models.CharField(verbose_name='model', max_length=64)

    class Meta:
        unique_together = ['make', 'model']

    def __str__(self):
        return f'Make: {self.make}, model: {self.model}'
