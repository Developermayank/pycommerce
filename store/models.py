from django.db import models
from django_jsonform.models.fields import JSONField

# Create your models here.

class Configuration(models.Model):
    group = models.PositiveSmallIntegerField(choices=[(1,'General'),(2,'Taxation'),(3,'Shipping'),], default=1)
    key = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    value = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'
        unique_together = ['group','key']
        ordering = ['group','key']

    def __str__(self):
        return self.key
