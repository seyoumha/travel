# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-27 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy', '0004_auto_20171127_1925'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Travler',
            new_name='Trips',
        ),
        migrations.AlterField(
            model_name='trips',
            name='travler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels', to='travel_buddy.Travel'),
        ),
    ]
