from django.db import models
from django.conf import settings
# Create your models here.

class CustomerGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    require_approval = models.BooleanField("Approve New Customers", default=False)
    sort_order = models.PositiveSmallIntegerField(blank=True, default=1)

    class Meta:
        verbose_name = 'Customer Group'
        verbose_name_plural = 'Customer Groups'

    def __str__(self):
        return self.name