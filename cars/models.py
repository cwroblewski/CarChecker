from django.db import models

RATES_CHOICES = [
    ('1', 'Very bad'),
    ('2', 'Bad'),
    ('3', 'Ok'),
    ('2', 'Good'),
    ('2', 'Very good'),
]


class Registry(models.Model):
    """Object create and modified dates model."""

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Car(Registry):
    """Car model."""

    make = models.CharField(verbose_name='marka', max_length=64)
    model = models.CharField(verbose_name='model', max_length=64)

    def __str__(self):
        return f'Marka: {self.make}, model: {self.model}'


class Rate(Registry):
    """Rate model."""

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rate = models.CharField(verbose_name='ocena uzytkowników', max_length=2, choices=RATES_CHOICES, blank=True)

    def __str__(self):
        return f'Samochód: {self.car}, Ocena: {self.rate}'
