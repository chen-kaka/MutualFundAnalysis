# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-09 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0021_fundrecommend_totalstart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mutualfundrating',
            name='fundType',
            field=models.CharField(max_length=100),
        ),
    ]