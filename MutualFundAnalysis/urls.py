# -*- coding: utf-8 -*-
"""DjangoProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

from Controller import fetchMutualData
from MutualFundAnalysis import search
from MutualFundAnalysis.testdb import testdb,testdbList,testdbUpdate,testdbDelete
from MutualFundAnalysis.view import hello

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'hello/$', hello),
    url(r'^testdb/$', testdb),
    url(r'^testdb_list/$', testdbList),
    url(r'^testdb_update/$', testdbUpdate),
    url(r'^testdb_delete/$', testdbDelete),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search.search_post),
    # 基金信息获取
    # http://localhost:8000/mutual_fund/fetch_data
    url(r'^mutual_fund/fetch_data/$', fetchMutualData.fetchMutualFundDataReq),
    # http://localhost:8000/mutual_fund/fetch_net_data
    url(r'^mutual_fund/fetch_net_data/$', fetchMutualData.fetchMutualFundNetDataReq),
    # http://localhost:8000/mutual_fund/fetch_bank_gold_data
    url(r'^mutual_fund/fetch_bank_gold_data/$', fetchMutualData.fetchBankGoldDataReq),
    # http://localhost:8000/mutual_fund/fetch_rating?date=2017-02-17
    url(r'^mutual_fund/fetch_rating/$', fetchMutualData.fetchFundRatingReq),
    # http://localhost:8000/mutual_fund/fetch_buyinfo
    # 获取基金的费率等信息，晨星接口已经没有这些信息了。
    # 之后需要再拉取其他的接口
    url(r'^mutual_fund/fetch_buyinfo/$', fetchMutualData.fetchFundBuyInfoReq),
    # http://localhost:8000/mutual_fund/fetch_returninfo
    url(r'^mutual_fund/fetch_returninfo/$', fetchMutualData.fetchFundReturnInfoReq),
    # http://localhost:8000/mutual_fund/fetch_managerinfo
    url(r'^mutual_fund/fetch_managerinfo/$', fetchMutualData.fetchFundManagerInfoReq),
    # http://localhost:8000/mutual_fund/fetch_managerdetail
    url(r'^mutual_fund/fetch_managerdetail/$', fetchMutualData.fetchFundManagerDetailReq),
    # http://localhost:8000/mutual_fund/fetch_fundselect
    url(r'^mutual_fund/fetch_fundselect/$', fetchMutualData.fetchFundSelectReq),
    # http://localhost:8000/mutual_fund/fetch_fundrecomend
    url(r'^mutual_fund/fetch_fundrecomend/$', fetchMutualData.fetchFundRecomendReq)
]
