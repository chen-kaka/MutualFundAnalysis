# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def requestData(reqUrl):
    responseHtml = requests.get(reqUrl)
    return responseHtml

def fetchMutualFundRatingData():
    print "fetchMutualFundRatingData start."
    url = "https://cn2.morningstar.com/handler/fundranking.ashx?fund=&category=stock&rating=&company=&cust=&sort=ReturnYTD&direction=desc&tabindex=0"
    #&date=2017-02-17&pageindex=1&pagesize=20"
    date = "2017-02-17"
    pageindex = 1
    pagesize = 20
    reqUrl = url + "&date=" + date + "&pageindex=" + bytes(pageindex) + "&pagesize=" + bytes(pagesize)
    print "reqUrl is:", reqUrl
    responseHtml = requestData(reqUrl)
    # print "responseHtml is: ", responseHtml
    soup = BeautifulSoup(responseHtml.text, "html.parser")
    print soup.prettify()
    targetTable = soup.html.body

fetchMutualFundRatingData()