# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
#CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
#晨星基金排名
class MutualFundRating(models.Model):
    code = models.CharField(max_length=50)               # 基金代码
    name = models.CharField(max_length=200)                # 基金名称
    fundType = models.CharField(max_length=100)                # 基金类型
    nav = models.FloatField()              # 单位净值
    StarRating3 = models.FloatField()         # 晨星三年评级
    StarRating5 = models.FloatField()         # 晨星五年评级
    SD3Year = models.FloatField()            # 三年波动幅度
    SD3YearComment = models.CharField(max_length=200)      # 三年波动幅度评价
    DR3Year = models.FloatField()           # 三年晨星风险系数,  越低越好
    DR3YearComment = models.CharField(max_length=200)      # 三年晨星风险系数评价
    SR3Year = models.FloatField()            # 三年夏普比例,  越高越好
    SR3YearComment = models.CharField(max_length=200)      # 三年夏普比例评价
    ReturnYTD = models.FloatField()           # 今年总回报率
    updateDate = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name


#晨星基金购买信息
class MutualFundBuyInfo(models.Model):
    code = models.CharField(max_length=50)                  # 基金代码
    name = models.CharField(max_length=200)                 # 基金名称
    establishDate = models.CharField(max_length=200)         # 成立日期
    applyState = models.CharField(max_length=200)             # 申购状态
    returnState = models.CharField(max_length=200)         # 赎回状态
    minBuy = models.FloatField()                           # 最小投资额
    frontCharge = models.FloatField()                       # 前端收费
    backCharge = models.FloatField()                       # 后端收费
    redeemFee = models.FloatField()                      # 赎回费
    manageFee = models.FloatField()                       # 管理费
    trusteeFee = models.FloatField()                      # 托管费
    serviceFee = models.FloatField()                      # 销售服务费
    updateDate = models.CharField(max_length=200)         #更新日期
    def __unicode__(self):
        return self.name


#晨星基金回报信息
class MutualFundReturnInfo(models.Model):
    code = models.CharField(max_length=50)                  # 基金代码
    name = models.CharField(max_length=200)                 # 基金名称
    oneDayReturn = models.FloatField()                     # 一天回报
    oneWeekReturn = models.FloatField()                       # 1周回报
    oneMonthReturn = models.FloatField()                     # 1个月回报
    threeMonthReturn = models.FloatField()                     # 3个月回报
    sixMonthReturn = models.FloatField()                       # 6个月回报
    oneYearReturn = models.FloatField()                       # 1年回报
    twoYearReturn = models.FloatField()                      # 2年年化回报
    threeYearReturn = models.FloatField()                       # 3年年化回报
    fiveYearReturn = models.FloatField()                      # 5年年化回报
    tenYearReturn = models.FloatField()                      # 10年年化回报
    totalReturn = models.FloatField()                       #设立以来回报
    threeYearStandard = models.FloatField()                #三年标准差
    threeYearRisk = models.FloatField()                     #三年晨星风险系数
    updateDate = models.CharField(max_length=200)         #更新日期
    def __unicode__(self):
        return self.name

#晨星经理信息
class MutualFundManagerInfo(models.Model):
    code = models.CharField(max_length=50)                  # 基金代码
    name = models.CharField(max_length=200)                 # 基金名称
    fundType = models.CharField(max_length=200)                # 基金类型
    fundScale = models.FloatField()                       # 基金规模(亿)
    manager = models.CharField(max_length=200)                     # 基金经理
    managerId = models.CharField(max_length=200,default='')                     # 基金经理ID
    totalStart = models.DateField()                     # 累计公募任职开始时间
    totalLength = models.IntegerField()                     # 累计公募任职长度
    manageStart = models.DateField()                       # 任职开始时间
    manageLength = models.IntegerField()                       # 任职长度
    manageAchive = models.FloatField()                       # 管理期业绩
    manageAvgAchive = models.FloatField()                      # 管理期同类平均业绩
    updateDate = models.CharField(max_length=200)         #更新日期
    def __unicode__(self):
        return self.name

#晨星基金经理详细信息
class MutualFundManagerDetail(models.Model):
    manager = models.CharField(max_length=200)                     # 基金经理
    managerId = models.CharField(max_length=200)       # 基金经理ID
    resum = models.CharField(max_length=1000,default='')       # 基金经理介绍
    code = models.CharField(max_length=50)                  # 基金代码
    name = models.CharField(max_length=200)                 # 基金名称
    manageStart = models.CharField(max_length=200)                 # 任职开始日期
    manageStartDate = models.DateField()                       # 任职开始时间
    manageEnd = models.CharField(max_length=200)                       # 任职结束日期
    manageEndDate = models.DateField()                       # 任职结束时间
    length = models.IntegerField()                       # 任职结束时任职长度
    onPosition = models.IntegerField()                       # 是否在任职 1: 是 0: 否
    manageAchive = models.FloatField()                       # 管理期业绩
    manageAvgAchive = models.FloatField()                      # 管理期同类平均业绩
    updateDate = models.CharField(max_length=200)         #更新日期
    def __unicode__(self):
        return self.name
















