# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from Service import fetchFundData,fetchNetData,fetchBankGoldData
from DataCrawler import Requester

#拉取基金基本数据
def fetchMutualFundDataReq(request):
    responseData = fetchFundData.fetchMutualFundData()
    return HttpResponse(json.dumps(responseData), content_type="application/json")

#拉取基金净值数据
def fetchMutualFundNetDataReq(request):
    responseData = fetchNetData.fetchNetDataReq()
    return HttpResponse(json.dumps(responseData), content_type="application/json")

#拉取银行黄金数据
def fetchBankGoldDataReq(request):
    responseData = fetchBankGoldData.fetchBankGoldDataReq()
    return HttpResponse(json.dumps(responseData), content_type="application/json")

#拉取排名数据
def fetchFundRatingReq(request):
    request.encoding='utf-8'
    reqDate = ''
    if 'date' in request.GET:
        reqDate = request.GET['date'].encode('utf-8')
    responseData = Requester.pagingFechMutualFundRatingData(reqDate)
    return HttpResponse(json.dumps(responseData), content_type="application/json")