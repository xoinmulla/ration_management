# Generated by Django 5.1.7 on 2025-03-13 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RationCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=20, unique=True)),
                ('holder_name', models.CharField(max_length=100)),
                ('card_type', models.CharField(choices=[('APL', 'Above Poverty Line'), ('BPL', 'Below Poverty Line')], max_length=3)),
                ('issued_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RationCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RationDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributed_items', models.TextField()),
                ('distribution_date', models.DateField()),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ration.rationcenter')),
                ('ration_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ration.rationcard')),
            ],
        ),
    ]
