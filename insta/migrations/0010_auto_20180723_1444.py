# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0009_auto_20180723_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comment',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(default='Tri'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='com', to='insta.Image'),
        ),
    ]
