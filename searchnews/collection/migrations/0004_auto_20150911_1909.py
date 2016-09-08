# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='id',
        ),
        migrations.AddField(
            model_name='page',
            name='page_id',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
        ),
    ]
