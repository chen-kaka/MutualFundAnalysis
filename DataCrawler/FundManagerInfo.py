# -*- coding: utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup
from Model.morningstar import MutualFundManagerInfo
from Service.common import convertStringToFloat,convertDateStringToInt


def fetchMutualFundManagerData():
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    reqUrl = "http://cn2.morningstar.com/fundmanagers/default.aspx"
    print "reqUrl is:", reqUrl

    # tmp = open("/Users/kakachan/Desktop/fundmanager.htm")
    # print "BeautifulSoup processing."
    # soup = BeautifulSoup(tmp, "lxml")

    responseHtml = requestData(reqUrl)
    print "BeautifulSoup processing."
    soup = BeautifulSoup(responseHtml.text, "lxml")
    # print responseHtml.text
    # print soup.prettify()

    targetTables = soup.findAll("table",style="width:100%; border-collapse:collapse;")
    print "targetTables length: ",len(targetTables)
    for ind in range(0,len(targetTables)):
        targetTable = targetTables[ind]
        # print "targetTable:",targetTable
        trs = targetTable.findAll('tr')
        for index in range(1,len(trs)):
            tr = trs[index]
            tds = tr.findAll('td')
            print "len: ", len(tds),"tds[0]:",tds[0]
            if len(tds) != 9:
                continue

            code = tds[0].find("a").get_text()

            newMutualFundManagerInfo = MutualFundManagerInfo.objects.filter(code=code)
            if newMutualFundManagerInfo :
                newMutualFundManagerInfo = newMutualFundManagerInfo[0]
                print "get MutualFundManagerInfo saved info is: ", MutualFundManagerInfo
            else:
                print "get MutualFundManagerInfo saved info is null, create new one.code:",code
                newMutualFundManagerInfo = MutualFundManagerInfo(code=code)

            i = 1
            newMutualFundManagerInfo.name = tds[i].find("a").get_text()
            i += 1
            newMutualFundManagerInfo.fundType = tds[i].get_text()
            i += 1
            newMutualFundManagerInfo.fundScale = convertStringToFloat(tds[i].get_text())
            i += 2
            newMutualFundManagerInfo.manager = tds[i].find("a").get_text()
            managersrc = tds[i].find("a").get('href')  #managerhistory.aspx?managerid=2125634
            newMutualFundManagerInfo.managerId = managersrc.split('=')[1]

            totalLength = convertDateStringToInt(tds[i].get_text())
            newMutualFundManagerInfo.totalLength  = totalLength
            newMutualFundManagerInfo.totalStart = time.strftime('%Y-%m-%d',time.localtime(time.time() - totalLength*24*60*60))
            i += 1
            manageLength = convertDateStringToInt(tds[i].get_text())
            newMutualFundManagerInfo.manageLength = manageLength
            newMutualFundManagerInfo.manageStart = time.strftime('%Y-%m-%d',time.localtime(time.time() - manageLength*24*60*60))
            i += 1
            newMutualFundManagerInfo.manageAchive = convertStringToFloat(tds[i].get_text())
            i += 1
            newMutualFundManagerInfo.manageAvgAchive = convertStringToFloat(tds[i].get_text())
            newMutualFundManagerInfo.updateDate = date
            newMutualFundManagerInfo.save()
    return {"msg":"ok"}

def requestData(reqUrl):
    responseHtml = requests.get(reqUrl)

    return responseHtml

# fetchMutualFundBuyData()