# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
#CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
#主要财务指标
# "code":"550017",
# "name":"信诚添金分级债券",
# "netincome":"--",
# "assincome":"0.2151",
# "netassrate":"--",
# "netgrowrate":"-0.8900",
# "tonetgrora":"29.3700",
# "time":"20160630"
class FundFinance(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    netincome = models.FloatField()
    assincome = models.FloatField()
    netassrate = models.FloatField()
    netgrowrate = models.FloatField()
    tonetgrora = models.FloatField()
    time = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

# 基金规模
# "code":"560003",
# "name":"益民创新优势混合",
# "fundshare":"986,718,250.3100",
# "netfunval":"844,465,274.72",
# "tolassfund":"853,366,706.31",
# "time":"20161231"
class FundScale(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    fundshare = models.FloatField()
    netfunval = models.FloatField()
    tolassfund = models.FloatField()
    time = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

# 资产配置
# "code":"560003",
# "name":"益民创新优势混合",
# "totalass":"853,366,720.00",
# "stockinv":"689,494,020.00",
# "stockrat":"80.800",
# "bondcurr":"84,010,584.00",
# "bcrate":"9.840",
# "time":"20161231"
class FundConfig(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    totalass = models.FloatField()
    stockinv = models.FloatField()
    stockrat = models.FloatField()
    bondcurr = models.FloatField()
    bcrate = models.FloatField()
    time = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

# 净值数据
# "jjlx":"偏股型基金",
# "nav_a":"0.0028",
# "nav_date":"2017-02-14",
# "nav_rate":"0.2537",
# "per_nav":"1.1066",
# "sg_states":"开放",
# "sname":"泰达宏利首选企业股票",
# "symbol":"162208",
# "total_nav":"1.8266",
# "yesterday_nav":"1.1038"
class FundNetData(models.Model):
    symbol = models.CharField(max_length=50)
    sname = models.CharField(max_length=200)
    jjlx = models.CharField(max_length=100)
    nav_a = models.FloatField()
    nav_date = models.CharField(max_length=100)
    nav_rate = models.FloatField()
    per_nav = models.FloatField()
    sg_states = models.CharField(max_length=100)
    total_nav = models.FloatField()
    yesterday_nav = models.FloatField()
    def __unicode__(self):
        return self.sname

# 银行黄金数据
# "variety":"美元账户黄金",
# "midpri":"1226.10",
# "buypri":"1224.60",
# "sellpri":"1227.60",
# "maxpri":"1230.58",
# "minpri":"1222.56",
# "todayopen":"1223.02",
# "closeyes":"1223.61",
# "quantpri":"1.00",
# "time":"2017-02-15 19:07:00.0"
class BankGoldData(models.Model):
    variety = models.CharField(max_length=200)
    midpri = models.FloatField()
    buypri = models.FloatField()
    sellpri = models.FloatField()
    maxpri = models.FloatField()
    minpri = models.FloatField()
    todayopen = models.FloatField()
    closeyes = models.FloatField()
    quantpri = models.FloatField()
    time = models.CharField(max_length=200)
    def __unicode__(self):
        return self.variety