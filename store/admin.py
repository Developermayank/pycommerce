from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('key','value', 'group')
    save_as = True
