# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mem_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='mem_host_owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='主机使用和者'),
        ),
        migrations.AddField(
            model_name='apply',
            name='host_id',
            field=models.ForeignKey(to='mem_list.Member', verbose_name='主机id'),
        ),
        migrations.AddField(
            model_name='apply',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='申请者'),
        ),
    ]
