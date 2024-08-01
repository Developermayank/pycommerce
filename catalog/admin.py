from typing import Any, Iterable
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.http import HttpRequest
from .models import *
# Register your models here.

class FilterValueInline(admin.TabularInline):
    model = FilterValue
    extra = 0

@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ('name','sort_order')
    inlines = [
        FilterValueInline,
    ]


class OptionValueInline(admin.TabularInline):
    model = OptionValue
    extra = 0

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name','sort_order')

    def get_inlines(self, request, obj):
        if obj and obj.type in ['select','checkbox','radio']:
            return [ OptionValueInline, ]
        return super().get_inlines(request, obj)


class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 0

@admin.register(AttributeGroup)
class AttributeGroupAdmin(admin.ModelAdmin):
    list_display = ('name','sort_order')
    inlines = [
        AttributeInline,
    ]