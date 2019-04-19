# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mem_list', '0005_auto_20190116_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='apply_status',
            field=models.SmallIntegerField(verbose_name='申请状态', choices=[(1, '申请中'), (2, '申请成功'), (3, '申请失败'), (4, '已撤销')], default=1),
        ),
    ]
