# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-20 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_auto_20180404_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='u2p_relation',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Event'),
            preserve_default=False,
        ),
    ]
