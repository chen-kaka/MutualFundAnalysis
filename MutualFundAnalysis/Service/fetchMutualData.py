# -*- coding: utf-8 -*-
import requests
import json
from django.http import HttpResponse
from Model.mutualfund import FundFinance, FundConfig, FundScale

# openid
OpenId = "JH86031efde94c219e84552800e01747f7"
# 主要财务指标
FundFinanceUrl = "http://web.juhe.cn:8080/fund/findata/main"
FundFinanceAppkey = "0c9511364511315c978dd45a22c7b271"

# 基金规模
FundScaleUrl = "http://web.juhe.cn:8080/fund/findata/size"
FundScaleAppkey = "0c9511364511315c978dd45a22c7b271"

# 资产配置
FundConfigUrl = "http://web.juhe.cn:8080/fund/findata/config"
FundConfigAppkey = "0c9511364511315c978dd45a22c7b271"

def fetchMutualDataReq(request):
    fundFinanceData = fetchMutualData(FundFinanceUrl, FundFinanceAppkey)
    fundScaleData = fetchMutualData(FundScaleUrl, FundScaleAppkey)
    fundConfigData = fetchMutualData(FundConfigUrl, FundConfigAppkey)

    for itemIndex, fundItem in fundFinanceData.iteritems():
        # 写入到数据库
        # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
        saveCode = fundItem["code"]
        time = fundItem["time"]
        print "fundItem:",fundItem,"saveCode:",saveCode
        savedInfo = FundFinance.objects.filter(code=saveCode)
        if savedInfo :
            savedInfo = savedInfo[0]
            if time == savedInfo.time:
                print "savedInfo not change, skip."
                continue
            print "get FundFinance saved info is: ", savedInfo
        else:
            print "get FundFinance saved info is null, create new one."
            savedInfo = FundFinance(code=saveCode)
        savedInfo.name = fundItem["name"]
        savedInfo.netincome = convertStringToFloat(fundItem["netincome"])
        savedInfo.assincome = convertStringToFloat(fundItem["assincome"])
        savedInfo.netassrate = convertStringToFloat(fundItem["netassrate"])
        savedInfo.netgrowrate = convertStringToFloat(fundItem["netgrowrate"])
        savedInfo.tonetgrora = convertStringToFloat(fundItem["tonetgrora"])
        savedInfo.time = fundItem["time"]
        print "savedInfo is:",savedInfo
        savedInfo.save()

    for itemIndex,fundItem in fundScaleData.iteritems():
        # 写入到数据库
        # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
        saveCode = fundItem["code"]
        time = fundItem["time"]
        savedInfo = FundScale.objects.filter(code=saveCode)
        if savedInfo :
            savedInfo = savedInfo[0]
            if time == savedInfo.time:
                print "savedInfo not change, skip."
                continue
            print "get FundScale saved info is: ", savedInfo
        else:
            print "get FundScale saved info is null, create new one."
            savedInfo = FundScale(code=saveCode)
        savedInfo.name = fundItem["name"]
        savedInfo.fundshare = convertStringToFloat(fundItem["fundshare"])
        savedInfo.netfunval = convertStringToFloat(fundItem["netfunval"])
        savedInfo.tolassfund = convertStringToFloat(fundItem["tolassfund"])
        savedInfo.time = fundItem["time"]
        print "savedInfo is:",savedInfo
        savedInfo.save()

    for itemIndex,fundItem in fundConfigData.iteritems():
        # 写入到数据库
        # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
        saveCode = fundItem["code"]
        time = fundItem["time"]
        savedInfo = FundConfig.objects.filter(code=saveCode)
        if savedInfo :
            savedInfo = savedInfo[0]
            if time == savedInfo.time:
                print "savedInfo not change, skip."
                continue
            print "get FundConfig saved info is: ", savedInfo
        else:
            print "get FundConfig saved info is null, create new one."
            savedInfo = FundConfig(code=saveCode)
        savedInfo.name = fundItem["name"]
        savedInfo.totalass = convertStringToFloat(fundItem["totalass"])
        savedInfo.stockinv = convertStringToFloat(fundItem["stockinv"])
        savedInfo.stockrat = convertStringToFloat(fundItem["stockrat"])
        savedInfo.bondcurr = convertStringToFloat(fundItem["bondcurr"])
        savedInfo.bcrate = convertStringToFloat(fundItem["bcrate"])
        savedInfo.time = fundItem["time"]
        print "savedInfo is:",savedInfo
        savedInfo.save()

    responseData = {
        "fundFinance" : len(fundFinanceData),
        "fundScale" : len(fundScaleData),
        "fundConfig" : len(fundConfigData)
    }
    return HttpResponse(json.dumps(responseData), content_type="application/json")

#转字符串为float
def convertStringToFloat(str):
    if str == None or str == "--" or str == "":
        return 0
    str = str.replace(",","")
    return float(str)

def fetchMutualData(reqUrl, appkey):
    params = {
        "key" : appkey, #APPKEY值
    }
    responseHtml = requests.post(reqUrl, data=params)
    responseJson = responseHtml.json()
    # print responseJson.text
    if responseJson["error_code"] == 0 :
        print "send reqUrl: " , reqUrl , ", fetch success."
        responseResult = responseJson["result"]
        if len(responseResult) > 0:
            responseResult = responseResult[0]
            print "reqUrl: " , reqUrl + ", fetch list size: " , len(responseResult)
            return responseResult
    return {}

