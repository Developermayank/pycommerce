from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name','code','status','sort_order')

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('title','code','value','updated_at')

@admin.register(StockStatus)
class StockStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(OrderStatus)
class OrderStatusAdmin(StockStatusAdmin):
    pass

@admin.register(SubscriptionStatus)
class SubscriptionStatusAdmin(StockStatusAdmin):
    pass

@admin.register(ReturnStatus)
class ReturnStatusAdmin(StockStatusAdmin):
    pass

@admin.register(ReturnAction)
class ReturnActionAdmin(StockStatusAdmin):
    pass

@admin.register(ReturnReason)
class ReturnReasonAdmin(StockStatusAdmin):
    pass


@admin.register(AddressFormat)
class AddressFormatAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','isocode_2', 'isocode_3')

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('country', 'name','code',)

@admin.register(GeoZone)
class GeoZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    filter_horizontal = ['zones',]


@admin.register(WeightClass)
class WeightClassAdmin(admin.ModelAdmin):
    list_display = ('title','unit', 'value')

@admin.register(LengthClass)
class LengthClassAdmin(admin.ModelAdmin):
    list_display = ('title','unit', 'value')


class TaxesInline(admin.TabularInline):
    model = Taxes
    extra = 0

@admin.register(TaxClass)
class TaxClassAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [
        TaxesInline,
    ]

@admin.register(TaxRate)
class TaxRateAdmin(admin.ModelAdmin):
    list_display = ('name','rate','type','geozone','created_at','updated_at')