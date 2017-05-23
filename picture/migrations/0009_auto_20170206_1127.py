# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import picture.models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0008_auto_20170205_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='created_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='picture',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image_path',
            field=models.ImageField(upload_to=picture.models.get_upload_image),
        ),
    ]