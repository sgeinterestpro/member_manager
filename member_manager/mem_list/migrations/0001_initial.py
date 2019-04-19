# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('fail_reason', models.CharField(verbose_name='失败原因', max_length=64)),
                ('remark', models.CharField(verbose_name='备注', max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('mem_ip', models.CharField(verbose_name='会员IP', max_length=15)),
                ('mem_login_name', models.CharField(verbose_name='会员登录名', max_length=64)),
                ('mem_login_pwd', models.CharField(verbose_name='会员登录密码', max_length=64)),
                ('mem_host_num', models.CharField(verbose_name='主机帐号编号', max_length=64)),
                ('mem_host_status', models.SmallIntegerField(default=1, verbose_name='主机状态', choices=[(1, '空闲'), (2, '被占用'), (3, '申请中')])),
                ('mem_remark', models.CharField(verbose_name='备注', max_length=64)),
            ],
            options={
                'db_table': 'mem_list',
            },
        ),
    ]
