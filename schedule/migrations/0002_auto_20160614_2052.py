# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='one_schedule',
        ),
        migrations.AddField(
            model_name='oneschedule',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.Person'),
        ),
    ]
