# Generated by Django 5.0.7 on 2024-08-01 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('format', models.TextField()),
            ],
            options={
                'verbose_name': 'Address Format',
                'verbose_name_plural': 'Address Formats',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('isocode_2', models.CharField(blank=True, max_length=2, verbose_name='ISO Code (2)')),
                ('isocode_3', models.CharField(blank=True, max_length=3, verbose_name='ISO Code (3)')),
                ('require_postcode', models.BooleanField(blank=True, default=False, verbose_name='Postcode Required')),
                ('status', models.BooleanField(default=True)),
                ('address_format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.addressformat')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
    ]