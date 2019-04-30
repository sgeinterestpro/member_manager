# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0003_remove_reserve_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='meeting',
        ),
    ]
