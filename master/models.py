from django.db import models
from customer.models import CustomerGroup

# Create your models here.

class StoreLocation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    telephone = models.CharField(max_length=15, blank=True)
    geocode = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d", blank=True)
    opening_time = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Store Location'
        verbose_name_plural = 'Store Locations'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=8)
    extension = models.CharField(max_length=255, blank=True)
    locale = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    sort_order = models.PositiveSmallIntegerField(default=1, blank=True)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name


class Currency(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=8)
    symbol_left = models.CharField(max_length=8, blank=True)
    symbol_right = models.CharField(max_length=8, blank=True)
    decimal_places = models.PositiveSmallIntegerField()
    value = models.FloatField(help_text="The value of your default currency in the current currency unit. Set to 1 for your default currency.")
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.title


class StockStatus(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Stock Status'
        verbose_name_plural = 'Stock Statuses'

    def __str__(self):
        return self.name


class OrderStatus(StockStatus):
    class Meta:
        verbose_name = 'Order Status'
        verbose_name_plural = 'Order Statuses'

class SubscriptionStatus(StockStatus):
    class Meta:
        verbose_name = 'Subscription Status'
        verbose_name_plural = 'Subscription Statuses'

class ReturnStatus(StockStatus):
    class Meta:
        verbose_name = 'Return Status'
        verbose_name_plural = 'Return Statuses'

class ReturnAction(StockStatus):
    class Meta:
        verbose_name = 'Return Action'
        verbose_name_plural = 'Return Actions'

class ReturnReason(StockStatus):
    class Meta:
        verbose_name = 'Return Reason'
        verbose_name_plural = 'Return Reasons'


class Country(models.Model):
    name = models.CharField(max_length=120, unique=True)
    isocode_2 = models.CharField("ISO Code (2)", max_length=2, blank=True)
    isocode_3 = models.CharField("ISO Code (3)", max_length=3, blank=True)
    address_format = models.ForeignKey('AddressFormat', on_delete=models.CASCADE)
    require_postcode = models.BooleanField("Postcode Required", default=False, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Zone(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=5, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'

    def __str__(self):
        return "%s - %s" % (self.country, self.name)

class GeoZone(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255, blank=True)
    zones = models.ManyToManyField(Zone)

    class Meta:
        verbose_name = 'Geo Zone'
        verbose_name_plural = 'Geo Zones'

    def __str__(self):
        return self.name


class WeightClass(models.Model):
    title = models.CharField(max_length=40, unique=True)
    unit = models.CharField(max_length=5)
    value = models.FloatField(blank=True)

    class Meta:
        verbose_name = 'Weight Class'
        verbose_name_plural = 'Weight Classes'

    def __str__(self):
        return self.title


class LengthClass(WeightClass):
    class Meta:
        verbose_name = 'Length Class'
        verbose_name_plural = 'Length Classes'


class AddressFormat(models.Model):
    name = models.CharField(max_length=50)
    format = models.TextField()

    class Meta:
        verbose_name = 'Address Format'
        verbose_name_plural = 'Address Formats'

    def __str__(self):
        return self.name


class TaxClass(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Tax Class'
        verbose_name_plural = 'Tax Classes'

    def __str__(self):
        return self.title


class TaxRate(models.Model):
    name = models.CharField(max_length=50)
    rate = models.FloatField()
    type = models.CharField(max_length=1, choices=[('P','Percentage'),('F','Fixed Amount')], default='P', blank=True)
    customergroups = models.ManyToManyField(CustomerGroup, verbose_name='Customer Groups')
    geozone = models.ForeignKey(GeoZone, on_delete=models.CASCADE, verbose_name='Geo Zone')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tax Rate'
        verbose_name_plural = 'Tax Rates'

    def __str__(self):
        return self.name


class Taxes(models.Model):
    taxclass = models.ForeignKey(TaxClass, on_delete=models.CASCADE)
    taxrate = models.ForeignKey(TaxRate, on_delete=models.CASCADE, verbose_name='Tax Rate')
    based_on = models.CharField(max_length=1, choices=[('A','Shipping Address'),('B','Payment Address'),('C','Store Address'),], default='A')
    priority = models.PositiveSmallIntegerField(blank=True, default=1)


    class Meta:
        verbose_name = 'Taxes'
        verbose_name_plural = 'Taxes'

    def __str__(self):
        return self.taxrate.name
