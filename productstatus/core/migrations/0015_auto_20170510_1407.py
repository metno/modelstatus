# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-10 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170510_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datainstance',
            name='deleted',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
