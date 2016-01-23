# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import fuel_price.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AAAData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=4)),
                ('location', models.CharField(max_length=64)),
                ('data', fuel_price.models.JSONField(blank=True, null=True)),
            ],
        ),
    ]