# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='allow_projects',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='allow_voting',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='groups',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='event',
            name='ideal_group_size',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='event',
            name='project_ideas',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
