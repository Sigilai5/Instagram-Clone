# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-22 15:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_auto_20180722_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]