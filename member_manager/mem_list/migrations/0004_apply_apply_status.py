# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mem_list', '0003_auto_20190107_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='apply_status',
            field=models.SmallIntegerField(verbose_name='申请状态', default=1, choices=[(1, '申请中'), (2, '申请成功'), (3, '申请失败')]),
        ),
    ]
