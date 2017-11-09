# -*- coding: utf-8 -*-

from Model.mutualfund import FundFinance, FundConfig, FundScale
from common import convertStringToFloat, fetchJuheData
import traceback

# 主要财务指标
FundFinanceUrl = "http://web.juhe.cn:8080/fund/findata/main"
FundFinanceAppkey = "0c9511364511315c978dd45a22c7b271"

# 基金规模
FundScaleUrl = "http://web.juhe.cn:8080/fund/findata/size"
FundScaleAppkey = "0c9511364511315c978dd45a22c7b271"

# 资产配置
FundConfigUrl = "http://web.juhe.cn:8080/fund/findata/config"
FundConfigAppkey = "0c9511364511315c978dd45a22c7b271"

def fetchMutualFundData():
    try:
        fundFinanceData = fetchMutualData(FundFinanceUrl, FundFinanceAppkey)
        fundScaleData = fetchMutualData(FundScaleUrl, FundScaleAppkey)
        fundConfigData = fetchMutualData(FundConfigUrl, FundConfigAppkey)

        for itemIndex, fundItem in fundFinanceData.iteritems():
            try:
                # 写入到数据库
                # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
                saveCode = fundItem["code"]
                fundTime = fundItem["time"]
                print "fundItem:",fundItem,"saveCode:",saveCode
                savedInfoList = FundFinance.objects.filter(code=saveCode)
                savedInfo = FundFinance()
                print "save info is: ", savedInfo
                if len(savedInfoList) > 0:
                    savedInfo = savedInfoList[0]
                    # if fundTime is not None:
                    #     fundTime = fundTime[0: 10]
                    print "=====time: ", fundTime, ", save time: ", savedInfo.time
                    if fundTime == savedInfo.time:
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
            except:
                traceback.print_exc()

        for itemIndex,fundItem in fundScaleData.iteritems():
            try:
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
            except:
                traceback.print_exc()

        for itemIndex,fundItem in fundConfigData.iteritems():
            try:
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
            except:
                traceback.print_exc()

        responseData = {
            "fundFinance" : len(fundFinanceData),
            "fundScale" : len(fundScaleData),
            "fundConfig" : len(fundConfigData)
        }
        return responseData
    except:
        traceback.print_exc()

def fetchMutualData(reqUrl, appkey):
    params = {
        "key" : appkey, #APPKEY值
    }
    return fetchJuheData(reqUrl, appkey, params)

