# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(max_length=10, default=datetime.datetime(2015, 11, 20, 3, 42, 59, 467660, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
