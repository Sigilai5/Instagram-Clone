# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-22 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0014_auto_20180722_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_caption',
        ),
        migrations.RemoveField(
            model_name='image',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='image',
            name='post_image',
        ),
    ]
