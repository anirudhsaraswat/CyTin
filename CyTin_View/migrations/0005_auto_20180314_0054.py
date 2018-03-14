# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-14 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CyTin_View', '0004_auto_20180312_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='software',
            old_name='isOs',
            new_name='isos',
        ),
        migrations.AddField(
            model_name='software',
            name='isRequested',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='software',
            name='requestedby',
            field=models.CharField(default='Admin', max_length=20),
        ),
    ]
