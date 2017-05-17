# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-17 01:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0033_auto_20170514_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='history',
            field=models.IntegerField(default=15, help_text='visible history in minutes'),
        ),
        migrations.AlterField(
            model_name='menutalkgrouplist',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.TalkGroupWithSystem'),
        ),
    ]