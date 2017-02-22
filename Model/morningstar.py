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














