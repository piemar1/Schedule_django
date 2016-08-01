# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 21:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0003_auto_20160711_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='akey_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 15, 21, 12, 29, 836094, tzinfo=utc)),
        ),
    ]