# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-22 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip_app', '0004_trip_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_created', to='login_app.User'),
        ),
    ]
