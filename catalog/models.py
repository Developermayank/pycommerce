from django.db import models

# Create your models here.
class Filter(models.Model):
    name = models.CharField(max_length=150)
    sort_order = models.PositiveSmallIntegerField(default=1, blank=True)

    class Meta:
        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'

    def __str__(self):
        return self.name

class FilterValue(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    sort_order = models.PositiveSmallIntegerField(default=1, blank=True)

    class Meta:
        verbose_name = 'Filter Value'
        verbose_name_plural = 'Filter Values'

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=150)
    TYPE_CHOICES = {
        "Coose": {
            "select": "Select", "radio": "Radio", "checkbox": "Checkbox",
        },
        "Input": {
            "text": "Text", "textarea": "Textarea",
        },
        "File": {
            "file": "File",
        },
        "Date": {
            "date": "Date", "time": "Time", "datetime": "Datetime",
        },
    }
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='select', blank=True)
    sort_order = models.PositiveSmallIntegerField(default=1, blank=True)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'

    def __str__(self):
        return self.name


class OptionValue(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, limit_choices_to={'type__in':['select','radio','checkbox']})
    value = models.CharField(max_length=150)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d", blank=True)
    sort_order = models.PositiveSmallIntegerField(default=1, blank=True)

    class Meta:
        verbose_name = 'Option Value'
        verbose_name_plural = 'Option Values'

    def __str__(self):
        return self.value


class AttributeGroup(models.Model):
    name = models.CharField(max_length=150)
    sort_order = models.PositiveSmallIntegerField(default=1, blank=True)

    class Meta:
        verbose_name = 'Attribute Group'
        verbose_name_plural = 'Attribute Groups'

    def __str__(self):
        return self.name

class Attribute(models.Model):
    attributegroup = models.ForeignKey(AttributeGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    sort_order = models.PositiveSmallIntegerField(default=1, blank=True)

    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'

    def __str__(self):
        return self.name