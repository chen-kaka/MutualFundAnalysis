# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0010_mutualfundreturninfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutualFundManagerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('fundType', models.CharField(max_length=200)),
                ('fundScale', models.FloatField()),
                ('manager', models.CharField(max_length=200)),
                ('totalStart', models.DateField()),
                ('totalLength', models.FloatField()),
                ('manageStart', models.DateField()),
                ('manageLength', models.FloatField()),
                ('manageAchive', models.FloatField()),
                ('manageAvgAchive', models.FloatField()),
                ('updateDate', models.CharField(max_length=200)),
            ],
        ),
    ]
