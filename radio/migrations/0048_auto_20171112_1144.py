# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-12 19:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0047_auto_20171112_1103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transmission',
            options={'ordering': ['-pk'], 'permissions': (('download_audio', 'Can download audio clips'),)},
        ),
    ]
