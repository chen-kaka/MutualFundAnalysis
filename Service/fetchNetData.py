# -*- coding: utf-8 -*-
from Model.mutualfund import FundNetData
from common import convertStringToFloat, fetchJuheData, fetchJuheDataResponse, fetchJuheDataSingleMap
import traceback

# 净值数据
FundNetDataUrl = "http://japi.juhe.cn/jingzhi/query.from"
FundNetDataAppkey = "f33b0222fe1e12579d7ffa39c965082b"

#类型

NetDataType = {
    "债券" : "zhaiquan", #债券
    "货币": "huobi", #货币
    "全部": "netvalue",# 全部
    "股票":"gupiao",# 股票
    "QDII":"qdii",# QDII
    "混合":"hunhe"# 混合
}

#入口
def fetchNetDataReq():
    try:
        fetchNetDataLength = fetchNetDataAndSaveToDb(FundNetDataUrl, FundNetDataAppkey, NetDataType["全部"])
        responseData = {
            "fetchNetData" : fetchNetDataLength
        }
        return responseData
    except:
        traceback.print_exc()

#拉取净值数据,分页拉取,并写入到DB
def fetchNetDataAndSaveToDb(reqUrl, appkey, type):
    params = {
        "key" : appkey, #APPKEY值
        "type" : type, # 类型
        "page" : 314,
        "pagesize" : 20
    }

    responseJson = fetchJuheDataResponse(reqUrl, appkey, params)

    totalLength = responseJson["total"]
    print "fetch net data type: ",type," total length is:",totalLength
    retData = responseJson["result"]
    print "fetch data length: ", len(retData)
    writeNetDataToDb(retData)

    retDataLength = len(retData)
    if retDataLength == 0:
        print "fetch juhe net data error. exit."
        return 0
    print "reqUrl: " , reqUrl + ", fetch list size: " , retDataLength

    totalReqPages = totalLength / params["pagesize"] + 1
    while params["page"] < totalReqPages:
        params["page"] = params["page"] + 1
        print "total page size: ", totalReqPages, ", fetching page num: ", params["page"]
        retData = fetchJuheDataSingleMap(reqUrl, appkey, params)
        print "fetch data length: ", len(retData)
        retDataLength += len(retData)
        writeNetDataToDb(retData)

    return retDataLength

#写入DB
def writeNetDataToDb(fundNetData):
    for fundItem in fundNetData:
        # 写入到数据库
        # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
        print "fundItem: ", fundItem
        symbol = fundItem["symbol"]
        nav_date = fundItem["nav_date"]
        savedInfo = FundNetData.objects.filter(symbol=symbol)
        if savedInfo :
            savedInfo = savedInfo[0]
            if nav_date == savedInfo.nav_date:
                print "savedInfo not change, skip."
                continue
            print "get FundNetData saved info is: ", savedInfo
        else:
            print "get FundNetData saved info is null, create new one."
            savedInfo = FundNetData(symbol=symbol)
        savedInfo.sname = fundItem["sname"]
        savedInfo.jjlx = fundItem["jjlx"]
        savedInfo.nav_a = convertStringToFloat(fundItem["nav_a"])
        savedInfo.nav_date = fundItem["nav_date"]
        savedInfo.nav_rate = convertStringToFloat(fundItem["nav_rate"])
        savedInfo.per_nav = convertStringToFloat(fundItem["per_nav"])
        savedInfo.sg_states = fundItem["sg_states"]
        savedInfo.total_nav = convertStringToFloat(fundItem["total_nav"])
        savedInfo.yesterday_nav = convertStringToFloat(fundItem["yesterday_nav"])
        print "savedInfo is:",savedInfo
        savedInfo.save()
