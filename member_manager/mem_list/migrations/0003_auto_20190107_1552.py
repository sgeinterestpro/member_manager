# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mem_list', '0002_auto_20190107_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mem_host_owner',
            field=models.ForeignKey(null=True, verbose_name='主机使用和者', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
