# -*- coding: utf-8 -*-

# import re
import time
import requests
import traceback
from bs4 import BeautifulSoup
from Model.morningstar import MutualFundRating
from Service.common import convertStringToFloat

fundType = {
    "stock":"股票型",
    "mix_radical":"激进配置型",
    "mix_flexible":"灵活配置型",
    "mix_standard":"标准混合型",
    "mix_keep":"保守混合型",
    "bond_convertible":"可转债",
    "bond_radical":"激进债券型",
    "bond_general":"普通债券型",
    "bond_pure":"纯债基金",
    "bond_short":"短债基金",
    "currency":"货币市场基金",
    "market_neutral":"市场中性策略",
    "commodities":"商品",
    "keep":"保本基金",
    "other":"其他"
}

def requestData(reqUrl):
    responseHtml = requests.get(reqUrl)
    return responseHtml

def categoryFetchMutualFundRatingData(reqDate = ''):
    try:
        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        if reqDate != '':
            date = reqDate

        print 'request date: ', date
        for category, categoryName in fundType.iteritems():
            print "type:",category,"name:",categoryName
            isDateCorrect = pagingFetchMutualFundRatingData(category,categoryName, date)
            if isDateCorrect == 0:
                return  {"msg":"date incorrect, exit."}
        return {"msg":"ok"}
    except:
        traceback.print_exc()

def pagingFetchMutualFundRatingData(category, categoryName, date):
    pagesize = 500
    totalCount = fetchMutualFundRatingData(category, categoryName, date, 1, pagesize)

    reqPages = totalCount / pagesize + 1
    print "req total pages: ", reqPages, " and totalCount: ", totalCount
    if totalCount == 0:
        return 0
    for index in range(1, reqPages):
        fetchMutualFundRatingData(category, categoryName, date, index+1, pagesize)
    return 1


def fetchMutualFundRatingData(category,categoryName, date, pageindex, pagesize):
    print "fetchMutualFundRatingData start.date: ",date,",pageindex: ",pageindex,",pagesize: ",pagesize
    url = "https://cn2.morningstar.com/handler/fundranking.ashx?fund=&rating=&company=&cust=&sort=ReturnYTD&direction=desc&tabindex=0"

    print "start fetch date: ",date," fund ranking data."
    reqUrl = url + "&category=" + category + "&date=" + date + "&pageindex=" + bytes(pageindex) + "&pagesize=" + bytes(pagesize)
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

        # for i in range(1,(len(tds))):
        #     td = tds[i]
        #     print td.get_text()

        rating3 = getRating(tds[4])
        rating5 = getRating(tds[5])
        print "rating3:",rating3,"rating5:",rating5
        i = 2
        newMutualFundRating.name = tds[i].get_text()
        i += 1
        newMutualFundRating.nav = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundRating.StarRating3 = rating3 # convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundRating.StarRating5 = rating5 # convertStringToFloat(tds[i].get_text())
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
        updateDate = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        newMutualFundRating.updateDate = updateDate
        newMutualFundRating.fundType = categoryName
        print "newMutualFundRating is:",newMutualFundRating
        newMutualFundRating.save()
    return totalCount

    # tr = soup.find('tr',attrs={"onmouseout": "this.style.background=''"})

# categoryFetchMutualFundRatingData()

def getRating(imgTag):
    imgTags = imgTag.findAll('img')
    rating = 0
    if len(imgTags) == 2:
        imgsrc = imgTags[0].get('src')
        if imgsrc.find("0") != -1:
            rating = 0
        elif imgsrc.find("1") != -1:
            rating = 1
        elif imgsrc.find("2") != -1:
            rating = 2
        elif imgsrc.find("3") != -1:
            rating = 3
        elif imgsrc.find("4") != -1:
            rating = 4
        elif imgsrc.find("5") != -1:
            rating = 5
    return rating