# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-22 11:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0003_remove_image_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='owner',
            field=models.ForeignKey(default='yes', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.CharField(default='yes', max_length=30),
        ),
    ]