# -*- coding: utf-8 -*-

import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#转字符串为float
def convertStringToFloat(str):
    if str == None or str == "--" or str == "" or str == "-":
        return 0
    str = str.replace(",","")
    return float(str)

def convertDateStringToInt(str): # xxd[3年315天] or [3年315天]  or 3年315天 or 315天 or 1年
    if str == None or str == "--" or str == "" or str == "-":
        return 0
    str = str.replace(" ","")
    if str.find('[') > 0: #舍弃掉[前面的中文名字
        str = str.split('[')[1]
    str = str.replace("[","").replace("]","").replace("天","")
    #切成两份
    yearsAndDays = str.split('年')
    if len(yearsAndDays) == 1:
            return int(yearsAndDays[0])
    print "yearsAndDays[0]:",yearsAndDays[0],"yearsAndDays[1]:",yearsAndDays[1]
    if yearsAndDays[1] == '':  #只有年没有天
        return int(yearsAndDays[0]) * 365
    return int(yearsAndDays[0]) * 365 + int(yearsAndDays[1])

#转字符串为float
def convertStringToFloatQoutExclude(str):
    if str == None or str == "--" or str == "" or str == "-":
        return 0
    str = str.replace(",","")
    str = str.replace("(份)","")
    str = str.replace("$","")
    return float(str)

def fetchJuheData(reqUrl, appkey, params):
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

def fetchJuheDataResponse(reqUrl, appkey, params):
    responseHtml = requests.post(reqUrl, data=params)
    responseJson = responseHtml.json()
    # print responseJson.text
    if responseJson["error_code"] == 0 :
        print "send reqUrl: " , reqUrl , ", fetch success."
        return responseJson
    return {}

def fetchJuheDataSingleMap(reqUrl, appkey, params):
    responseHtml = requests.post(reqUrl, data=params)
    responseJson = responseHtml.json()
    # print responseJson.text
    if responseJson["error_code"] == 0 :
        print "send reqUrl: " , reqUrl , ", fetch success."
        responseResult = responseJson["result"]
        print "reqUrl: " , reqUrl + ", fetch list size: " , len(responseResult)
        return responseResult
    return {}