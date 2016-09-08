# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_page_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('idx', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('index_table', models.CharField(max_length=3000)),
            ],
        ),
    ]
