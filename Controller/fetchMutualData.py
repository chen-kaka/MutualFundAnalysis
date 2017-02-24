# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from Service import fetchFundData,fetchNetData,fetchBankGoldData
from DataCrawler import Requester,FundBuyinfo,FundReturnInfo,FundManagerInfo,FundManagerDetail

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
    responseData = Requester.categoryFetchMutualFundRatingData(reqDate)
    return HttpResponse(json.dumps(responseData), content_type="application/json")

#拉取购买数据
def fetchFundBuyInfoReq(request):
    request.encoding='utf-8'
    responseData = FundBuyinfo.pagingFetchMutualFundBuyData()
    return HttpResponse(json.dumps(responseData), content_type="application/json")

#拉取回报数据
def fetchFundReturnInfoReq(request):
    request.encoding='utf-8'
    responseData = FundReturnInfo.pagingFetchMutualFundReturnData()
    return HttpResponse(json.dumps(responseData), content_type="application/json")

#拉取基金经理数据
def fetchFundManagerInfoReq(request):
    request.encoding='utf-8'
    responseData = FundManagerInfo.fetchMutualFundManagerData()
    return HttpResponse(json.dumps(responseData), content_type="application/json")

#拉取基金经理详细数据
def fetchFundManagerDetailReq(request):
    request.encoding='utf-8'
    responseData = FundManagerDetail.fetchMutualFundDetailData()
    return HttpResponse(json.dumps(responseData), content_type="application/json")