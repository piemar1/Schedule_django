# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsschedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('register_updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
