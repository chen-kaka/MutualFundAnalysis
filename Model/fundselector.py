# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
#CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
#晨星基金排名
class FundRecommend(models.Model):
    code = models.CharField(max_length=50)               # 基金代码
    name = models.CharField(max_length=200)                # 基金名称
    threeYearSharp = models.FloatField()            # 三年夏普比例,  越高越好
    threeYearStandard = models.FloatField()                #三年标准差  越小越稳定
    threeYearRisk = models.FloatField()                     #三年晨星风险系数  越低越好
    StarRating3 = models.FloatField()         # 晨星三年评级
    StarRating5 = models.FloatField()         # 晨星五年评级
    rank = models.IntegerField(default=0)              # 排名
    oneWeekReturn = models.FloatField(default=0)                       # 1周回报
    oneMonthReturn = models.FloatField(default=0)                     # 1个月回报
    threeMonthReturn = models.FloatField(default=0)                     # 3个月回报
    sixMonthReturn = models.FloatField(default=0)                       # 6个月回报
    oneYearReturn = models.FloatField(default=0)                       # 1年回报
    twoYearReturn = models.FloatField(default=0)                      # 2年年化回报
    threeYearReturn = models.FloatField(default=0)                       # 3年年化回报
    fiveYearReturn = models.FloatField(default=0)                      # 5年年化回报
    tenYearReturn = models.FloatField(default=0)                      # 10年年化回报
    totalReturn = models.FloatField(default=0)                       #设立以来回报

    manager = models.CharField(max_length=200)                     # 基金经理
    manageAchive = models.FloatField()                       # 管理期业绩
    manageAvgAchive = models.FloatField()                      # 管理期同类平均业绩

    updateDate = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
