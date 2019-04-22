# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-22 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('trip_app', '0003_auto_20190422_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='created_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_created', to='login_app.User'),
        ),
    ]