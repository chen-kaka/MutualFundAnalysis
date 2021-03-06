# -*- coding: utf-8 -*-

from Model.mutualfund import BankGoldData
from common import convertStringToFloat, fetchJuheData
import traceback
import time

# 银行黄金数据
BankGoldUrl = "http://web.juhe.cn:8080/finance/gold/bankgold"
BankGoldAppkey = "14616d65eb8aa99112839edb2a3470ad"


def fetchBankGoldDataReq():
    try:
        bankGoldData = fetchBankGoldData(BankGoldUrl, BankGoldAppkey)

        for itemIndex, fundItem in bankGoldData.iteritems():
            # 写入到数据库
            # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
            variety = fundItem["variety"]
            fundTime = fundItem["time"]
            print "fundItem:",fundItem,"save variety:",variety
            savedInfoList = BankGoldData.objects.filter(variety=variety)
            savedInfo = BankGoldData()
            if len(savedInfoList) > 0 :
                savedInfo = savedInfoList[0]
                if fundTime is not None:
                    fundTime = fundTime[0: 10]
                print "===fundTime: ", fundTime, ", save time: ", savedInfo.time
                if fundTime == savedInfo.time:
                    print "savedInfo not change, skip."
                    continue
                print "get BankGoldData saved info is: ", savedInfo
            else:
                print "get BankGoldData saved info is null, create new one."
                savedInfo = BankGoldData(variety=variety)
            savedInfo.midpri = convertStringToFloat(fundItem["midpri"])
            savedInfo.buypri = convertStringToFloat(fundItem["buypri"])
            savedInfo.sellpri = convertStringToFloat(fundItem["sellpri"])
            savedInfo.maxpri = convertStringToFloat(fundItem["maxpri"])
            savedInfo.minpri = convertStringToFloat(fundItem["minpri"])
            savedInfo.todayopen = convertStringToFloat(fundItem["todayopen"])
            savedInfo.closeyes = convertStringToFloat(fundItem["closeyes"])
            savedInfo.quantpri = convertStringToFloat(fundItem["quantpri"])
            # savedInfo.time = fundItem["time"]
            date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            savedInfo.time = date
            print "savedInfo is:",savedInfo
            savedInfo.save()

        responseData = {
            "bankGold" : len(bankGoldData)
        }
        return responseData
    except:
        traceback.print_exc()
    return {}

def fetchBankGoldData(reqUrl, appkey):
    params = {
        "key" : appkey, #APPKEY值
    }
    return fetchJuheData(reqUrl, appkey, params)

