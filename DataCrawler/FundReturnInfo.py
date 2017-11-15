# -*- coding: utf-8 -*-

import time
import requests
import traceback
from bs4 import BeautifulSoup
from Model.morningstar import MutualFundReturnInfo
from Service.common import convertStringToFloat
from Service.morningstar import fetchFirstPageViewStateInfo

def pagingFetchMutualFundReturnData():
    try:
        stateInfo = fetchFirstPageViewStateInfo()
        totalCount = fetchMutualFundReturnData(stateInfo)
        print "total totalCount: ", totalCount
    except:
        traceback.print_exc()
        return {"msg":"failed."}

def fetchMutualFundReturnData(stateInfo):
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    reqUrl = "http://cn2.morningstar.com/fundselect/default.aspx"
    print "reqUrl is:", reqUrl

    page= 1
    pageSize = 25
    data = {
        "__EVENTTARGET":"ctl00$cphMain$lbPerformance",
        "__EVENTARGUMENT":"",
        "__LASTFOCUS":"",
        "__VIEWSTATE":stateInfo,
        "ctl00$cphMain$hfStylebox":"0,0,0,0,0,0,0,0,0",
        "ctl00$cphMain$hfRisk":"0,0,0,0",
        "ctl00$cphMain$ucPerformance$YTD":"rbYtd2",
        "ctl00$cphMain$ucPerformance$txtYtd":"",
        "ctl00$cphMain$ucPerformance$Month3":"rbM32",
        "ctl00$cphMain$ucPerformance$txtM3":"",
        "ctl00$cphMain$ucPerformance$Month6":"rbM62",
        "ctl00$cphMain$ucPerformance$txtM6":"",
        "ctl00$cphMain$ucPerformance$Year1":"rbY12",
        "ctl00$cphMain$ucPerformance$txtY1":"",
        "ctl00$cphMain$ucPerformance$Year2":"rbY22",
        "ctl00$cphMain$ucPerformance$txtY2":"",
        "ctl00$cphMain$ucPerformance$Year3":"rbY32",
        "ctl00$cphMain$ucPerformance$txtY3":"",
        "ctl00$cphMain$ucPerformance$Year5":"rbY52",
        "ctl00$cphMain$ucPerformance$txtY5":"",
        "ctl00$cphMain$ucPerformance$Year10":"rbY102",
        "ctl00$cphMain$ucPerformance$txtY10":"",
        "ctl00$cphMain$ddlEffectiveDate":"G",
        "ctl00$cphMain$txtEffectiveDate":"",
        "ctl00$cphMain$ddlFundStatus":"",
        "ctl00$cphMain$hfTNA":"0~5",
        "ctl00$cphMain$hfMinInvest":"0~5",
        "ctl00$cphMain$txtFund":"",
        "ctl00$cphMain$hfMoreOptions":"close",
        "ctl00$cphMain$ddlPageSite":pageSize,
        "__EVENTARGUMENT": page
    }

    totalFetch = 0
    print "req data is: ", data
    totalCount = pageMutualFundReturnData(reqUrl, data, date)
    for page in range(2,totalCount/pageSize + 2):
        data["__EVENTARGUMENT"] = page
        print "req data is: ", data
        pageMutualFundReturnData(reqUrl, data, date)

    return totalCount

def pageMutualFundReturnData(reqUrl, data, date):
    responseHtml = requestData(reqUrl, data)
    soup = BeautifulSoup(responseHtml.text, "lxml")
    # print responseHtml.text
    # print soup.prettify()

    summaryData = soup.find(id='ctl00_cphMain_TotalResultLabel')
    print "summaryData: ", summaryData
    if summaryData == None or any(summaryData) == False:
        print "fetch fund buyinfo data error. exit."
        return 0
    totalCount = int(summaryData.get_text())
    print "totalCount: ", totalCount

    targetTable = soup.find(id="ctl00_cphMain_gridResult")
    trs = targetTable.findAll('tr')
    pageLength = len(trs)
    totalFetch += pageLength
    for index in range(1, pageLength):
        tr = trs[index]
        tds = tr.findAll('td')
        print "tr length: ", len(tds)
        code = tds[1].find("a").get_text()

        newMutualFundReturnInfo = MutualFundReturnInfo.objects.filter(code=code)
        if newMutualFundReturnInfo:
            newMutualFundReturnInfo = newMutualFundReturnInfo[0]
            print "get MutualFundReturnInfo saved info is: ", MutualFundReturnInfo
        else:
            print "get MutualFundReturnInfo saved info is null, create new one.code:", code
            newMutualFundReturnInfo = MutualFundReturnInfo(code=code)

        i = 2
        newMutualFundReturnInfo.name = tds[i].find("a").get_text()
        print "code:", code, "name:", newMutualFundReturnInfo.name
        i += 1
        newMutualFundReturnInfo.oneDayReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.oneWeekReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.oneMonthReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.threeMonthReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.sixMonthReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.oneYearReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.twoYearReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.threeYearReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.fiveYearReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.tenYearReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.totalReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.threeYearStandard = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.threeYearRisk = convertStringToFloat(tds[i].get_text())
        newMutualFundReturnInfo.updateDate = date
        print "newMutualFundReturnInfo is:", newMutualFundReturnInfo
        newMutualFundReturnInfo.save()
    return totalCount

def requestData(reqUrl, payload):
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding":"gzip, deflate, br",
        "Referer":"http://cn2.morningstar.com/quickrank/default.aspx",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Host":"cn2.morningstar.com",
        "Origin":"http://cn2.morningstar.com",
        "Cookie": "Cookie:BAIDU_SSP_lcr=https://www.baidu.com/link?url=qXDBs04d3uhjRer7II5sR53HLoM6-8awY6h4ftfbcPSJ0TDc-9NAK1gSM1KiXBGU5pxXXQf5EwvijnS0kwzQua&wd=&eqid=9d5ed8850002e19e000000035a07cbe4; ASP.NET_SessionId=dw5brkflfvroes55sxle2155; MS_LocalEmailAddr=chen-kaka@163.com=; user=username=chen-kaka@163.com&nickname=&status=&password=; BIGipServercn=2241287690.20480.0000; Hm_lvt_eca85e284f8b74d1200a42c9faa85464=1510459525; Hm_lpvt_eca85e284f8b74d1200a42c9faa85464=1510471903; __utmt=1; __utma=172984700.1666955223.1510459530.1510467618.1510471908.4; __utmb=172984700.1.10.1510471908; __utmc=172984700; __utmz=172984700.1510460404.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic"
    }
    responseHtml = requests.post(reqUrl, data=payload, headers=headers)

    return responseHtml

# fetchMutualFundBuyData()