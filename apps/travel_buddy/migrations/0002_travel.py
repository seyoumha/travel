# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-27 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('plan', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travel', to='travel_buddy.User')),
            ],
        ),
    ]
