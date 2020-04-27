# Generated by Django 2.2 on 2020-04-27 11:58

import data.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_migration_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='apifetch',
            name='apiKey',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=100), default=data.models.APIFetch.getDefaultAPIKeys, size=None),
        ),
        migrations.AddField(
            model_name='apifetch',
            name='fetchInterval',
            field=models.IntegerField(default=60),
        ),
        migrations.AddField(
            model_name='apifetch',
            name='searchQuery',
            field=models.CharField(default='', max_length=50),
        ),
    ]
