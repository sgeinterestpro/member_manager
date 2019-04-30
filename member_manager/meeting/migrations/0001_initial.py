# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('name', models.CharField(verbose_name='会议室名称', max_length=20)),
                ('address', models.CharField(verbose_name='会议室地址', max_length=30)),
                ('galleryful', models.IntegerField(verbose_name='容纳人数', max_length=50)),
            ],
            options={
                'db_table': 'Meetings',
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('title', models.CharField(verbose_name='会议内容', max_length=60)),
                ('start', models.TimeField(verbose_name='开始时间')),
                ('end', models.TimeField(verbose_name='结束时间')),
                ('timestamp', models.DateField(verbose_name='创建时间')),
                ('root', models.CharField(verbose_name='会议室', max_length=100)),
                ('meeting', models.ForeignKey(verbose_name='会议室', to='meeting.Meetings')),
                ('user', models.ForeignKey(verbose_name='预定人', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Reserve',
            },
        ),
    ]
