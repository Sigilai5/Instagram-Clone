# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 17:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0016_auto_20180723_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='by', to=settings.AUTH_USER_MODEL),
        ),
    ]
