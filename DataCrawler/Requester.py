# -*- coding: utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup
from Model.morningstar import MutualFundRating
from Service.common import convertStringToFloat

def requestData(reqUrl):
    responseHtml = requests.get(reqUrl)
    return responseHtml

def pagingFechMutualFundRatingData():
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    pageindex = 1
    pagesize = 20
    fetchMutualFundRatingData(date, pageindex, pagesize)

def fetchMutualFundRatingData(date, pageindex, pagesize):
    print "fetchMutualFundRatingData start."
    url = "https://cn2.morningstar.com/handler/fundranking.ashx?fund=&category=stock&rating=&company=&cust=&sort=ReturnYTD&direction=desc&tabindex=0"

    print "start fetch date: ",date," fund ranking data."
    reqUrl = url + "&date=" + date + "&pageindex=" + bytes(pageindex) + "&pagesize=" + bytes(pagesize)
    print "reqUrl is:", reqUrl
    # responseHtml = requestData(reqUrl)

    tt = open("/Users/kakachan/Desktop/fundranking.ashx.htm")
    soup = BeautifulSoup(tt, "lxml")

    # soup = BeautifulSoup(responseHtml.text, "lxml") #"html.parser")

    # print soup.prettify()
    targetTable = soup.findAll("table",class_="fr_tablecontent")
    trs = targetTable[0].findAll('tr')
    for index in range(0,len(trs)-1):
        tr = trs[index]
        tds = tr.findAll('td')
        print "len: ", len(tds)
        code = tds[1].get_text()
        newMutualFundRating = MutualFundRating.objects.filter(code=code)
        if newMutualFundRating :
            newMutualFundRating = newMutualFundRating[0]
            print "get MutualFundRating saved info is: ", MutualFundRating
        else:
            print "get BankGoldData saved info is null, create new one."
            newMutualFundRating = MutualFundRating(code=code)

        i = 2
        newMutualFundRating.name = tds[i].get_text()
        i += 1
        newMutualFundRating.nav = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundRating.StarRating3 = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundRating.StarRating5 = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundRating.SD3Year = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundRating.SD3YearComment = tds[i].get_text()
        i += 1
        newMutualFundRating.DR3Year = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundRating.DR3YearComment = tds[i].get_text()
        i += 1
        newMutualFundRating.SR3Year = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundRating.SR3YearComment = tds[i].get_text()
        i += 1
        newMutualFundRating.ReturnYTD = convertStringToFloat(tds[i].get_text())
        newMutualFundRating.updateDate = date
        print "newMutualFundRating is:",newMutualFundRating
        newMutualFundRating.save()
    return {"msg":"ok"}
        # for i in range(1,(len(tds))):
        #     td = tds[i]
        #     print td.get_text()
    # tr = soup.find('tr',attrs={"onmouseout": "this.style.background=''"})