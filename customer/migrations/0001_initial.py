# Generated by Django 5.0.7 on 2024-08-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('require_approval', models.BooleanField(default=False, verbose_name='Approve New Customers')),
                ('sort_order', models.PositiveSmallIntegerField(blank=True, default=1)),
            ],
            options={
                'verbose_name': 'Customer Group',
                'verbose_name_plural': 'Customer Groups',
            },
        ),
    ]