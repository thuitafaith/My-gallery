# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snaps', '0004_auto_20180503_0900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='location_name',
        ),
    ]