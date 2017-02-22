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