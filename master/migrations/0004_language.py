# Generated by Django 5.0.7 on 2024-08-01 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_zone_geozone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=8)),
                ('extension', models.CharField(blank=True, max_length=255)),
                ('locale', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('sort_order', models.PositiveSmallIntegerField(blank=True, default=1)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
    ]
