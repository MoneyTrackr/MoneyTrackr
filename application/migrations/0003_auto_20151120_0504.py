# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_category_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 5, 4, 1, 759041, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 5, 4, 13, 974926, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
