# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mem_list', '0004_apply_apply_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='host_id',
            new_name='host',
        ),
        migrations.RenameField(
            model_name='apply',
            old_name='user_id',
            new_name='user',
        ),
    ]
