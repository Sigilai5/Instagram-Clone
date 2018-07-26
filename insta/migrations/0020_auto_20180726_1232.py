# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 09:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0019_auto_20180725_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
