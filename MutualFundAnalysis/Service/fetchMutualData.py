# -*- coding: utf-8 -*-
import requests
import json
from django.http import HttpResponse

# openid
OpenId = "JH86031efde94c219e84552800e01747f7"
# 主要财务指标
FundFinanceUrl = "http://web.juhe.cn:8080/fund/findata/main"
FundFinanceAppkey = "0c9511364511315c978dd45a22c7b271"
''''
assincome
:
"0.2151"
code
:
"550017"
name
:
"信诚添金分级债券"
netassrate
:
"--"
netgrowrate
:
"-0.8900"
netincome
:
"--"
time
:
"20160630"
tonetgrora
:
"29.3700"'''

# 基金规模
FundScaleUrl = "http://web.juhe.cn:8080/fund/findata/size"
FundScaleAppkey = "0c9511364511315c978dd45a22c7b271"

'''
code
:
"560003"
fundshare
:
"986,718,250.3100"
name
:
"益民创新优势混合"
netfunval
:
"844,465,274.72"
time
:
"20161231"
tolassfund
:
"853,366,706.31"'''

# 资产配置
FundConfigUrl = "http://web.juhe.cn:8080/fund/findata/config"
FundConfigAppkey = "0c9511364511315c978dd45a22c7b271"

'''
bcrate
:
""
bondcurr
:
""
code
:
"560006"
name
:
"益民核心增长混合"
stockinv
:
"31,425,822.00"
stockrat
:
"74.120"
time
:
"20161231"
totalass
:
"42,398,012.00"'''

def fetchMutualDataReq(request):
    fundFinanceData = fetchMutualData(FundFinanceUrl, FundFinanceAppkey)
    fundScaleData = fetchMutualData(FundScaleUrl, FundScaleAppkey)
    fundConfigData = fetchMutualData(FundConfigUrl, FundConfigAppkey)
    responseData = {
        "fundFinance" : fundFinanceData,
        "fundScale" : fundScaleData,
        "fundConfig" : fundConfigData
    }
    return HttpResponse(json.dumps(responseData), content_type="application/json")

def fetchMutualData(reqUrl, appkey):
    params = {
        "key" : appkey, #APPKEY值
    }
    responseHtml = requests.post(reqUrl, data=params)
    responseJson = responseHtml.json()
    # print responseJson.text
    if(responseJson["error_code"] == 0):
        print "send reqUrl: " + reqUrl + ", fetch success."
        responseResult = responseJson["result"]
        return responseResult
    return []

