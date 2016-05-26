# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letsschedule', '0006_auto_20160524_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='crew',
        ),
        migrations.AddField(
            model_name='person',
            name='crew',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='letsschedule.Team'),
        ),
    ]
