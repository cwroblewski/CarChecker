from django.db import models


class Registry(models.Model):
    """Object create and modified dates model."""

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True