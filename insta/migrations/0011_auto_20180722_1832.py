# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-22 15:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0010_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='owner',
            field=models.ForeignKey(default='yes', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='post_image',
            field=models.ImageField(default='card', upload_to='post/'),
        ),
    ]