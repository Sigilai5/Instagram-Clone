# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insta.Comments'),
        ),
    ]
