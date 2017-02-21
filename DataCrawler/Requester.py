# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import lxml

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
    # responseHtml = requestData(reqUrl)
    # print "responseHtml is: ", responseHtml
    tt = open("/Users/kakachan/Desktop/fundranking.ashx.htm");
    # soup = BeautifulSoup(responseHtml.text, "html.parser")
    soup = BeautifulSoup(tt, "lxml")

    # print soup.prettify()
    targetTable = soup.findAll("table",class_="fr_tablecontent")
    # print targetTable
    trs = targetTable[0].findAll('tr')
    for index in range(0,len(trs)-1):
        tr = trs[index]
        tds = tr.findAll('td')
        print "len: ", len(tds)
        for i in range(1,(len(tds))):
            td = tds[i]
            print td.get_text()

    # tr = soup.find('tr',attrs={"onmouseout": "this.style.background=''"})

fetchMutualFundRatingData()