# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180531_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]