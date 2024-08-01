# Generated by Django 5.0.7 on 2024-08-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_option_remove_filter_filtergroup_filtervalue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionvalue',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='optionvalue',
            name='sort_order',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='optionvalue',
            name='value',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]