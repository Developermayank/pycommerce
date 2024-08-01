# Generated by Django 5.0.7 on 2024-08-01 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('master', '0007_taxrate_customergroups'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Tax Class',
                'verbose_name_plural': 'Tax Classes',
            },
        ),
        migrations.AlterField(
            model_name='taxrate',
            name='customergroups',
            field=models.ManyToManyField(to='customer.customergroup', verbose_name='Customer Groups'),
        ),
        migrations.AlterField(
            model_name='taxrate',
            name='geozone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.geozone', verbose_name='Geo Zone'),
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('based_on', models.CharField(choices=[('A', 'Shipping Address'), ('B', 'Payment Address'), ('C', 'Store Address')], default='A', max_length=1)),
                ('priority', models.PositiveSmallIntegerField(blank=True, default=1)),
                ('taxclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.taxclass')),
                ('taxrate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.taxrate', verbose_name='Tax Rate')),
            ],
            options={
                'verbose_name': 'Taxes',
                'verbose_name_plural': 'Taxes',
            },
        ),
    ]
