# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_remove_reserve_meeting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='end',
            field=models.CharField(max_length=60, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='start',
            field=models.CharField(max_length=60, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='timestamp',
            field=models.CharField(max_length=60, verbose_name='创建时间'),
        ),
    ]
