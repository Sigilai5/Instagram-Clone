# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-22 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_image_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='post_image',
            field=models.ImageField(default='card', upload_to='post/'),
        ),
    ]
