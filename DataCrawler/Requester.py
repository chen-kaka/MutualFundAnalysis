# -*- coding: utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup
from Model.morningstar import MutualFundRating
from Service.common import convertStringToFloat

def requestData(reqUrl):
    responseHtml = requests.get(reqUrl)
    return responseHtml

def pagingFechMutualFundRatingData(reqDate = ''):
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if reqDate != '':
        date = reqDate

    print 'request date: ', date

    pagesize = 500
    totalCount = fetchMutualFundRatingData(date, 1, pagesize)

    reqPages = totalCount / pagesize + 1
    print "req total pages: ", reqPages
    for index in range(1, reqPages):
        fetchMutualFundRatingData(date, index+1, pagesize)
    return {"msg":"ok"}

def fetchMutualFundRatingData(date, pageindex, pagesize):
    print "fetchMutualFundRatingData start.date: ",date,",pageindex: ",pageindex,",pagesize: ",pagesize
    url = "https://cn2.morningstar.com/handler/fundranking.ashx?fund=&category=stock&rating=&company=&cust=&sort=ReturnYTD&direction=desc&tabindex=0"

    print "start fetch date: ",date," fund ranking data."
    reqUrl = url + "&date=" + date + "&pageindex=" + bytes(pageindex) + "&pagesize=" + bytes(pagesize)
    print "reqUrl is:", reqUrl

    # tmp = open("/Users/kakachan/Desktop/fundranking.ashx.htm")
    # soup = BeautifulSoup(tmp, "lxml")

    responseHtml = requestData(reqUrl)
    soup = BeautifulSoup(responseHtml.text, "lxml") #"html.parser")

    # print soup.prettify()

    #获取一共多少条数据
    summaryDatas = soup.find_all('span',style='color:#1E50A2; font-family:Arial;')
    print "summaryDatas: ",summaryDatas
    if len(summaryDatas) == 0:
        print "fetch mutual fund data error. exit."
        return 0
    totalCount =int(summaryDatas[1].get_text())
    print "totalCount: ",totalCount

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
    return totalCount
        # for i in range(1,(len(tds))):
        #     td = tds[i]
        #     print td.get_text()
    # tr = soup.find('tr',attrs={"onmouseout": "this.style.background=''"})