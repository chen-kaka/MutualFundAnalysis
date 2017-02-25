# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
#CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
#晨星基金排名
class FundRecommend(models.Model):
    code = models.CharField(max_length=50)               # 基金代码
    name = models.CharField(max_length=200)                # 基金名称
    updateDate = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
