# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from Service import fetchFundData,fetchNetData


#拉取基金基本数据
def fetchMutualFundDataReq(request):
    responseData = fetchFundData.fetchMutualFundData()
    return HttpResponse(json.dumps(responseData), content_type="application/json")

#拉取基金净值数据
def fetchMutualFundNetDataReq(request):
    responseData = fetchNetData.fetchNetDataReq()
    return HttpResponse(json.dumps(responseData), content_type="application/json")