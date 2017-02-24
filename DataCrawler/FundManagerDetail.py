# -*- coding: utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup
from Model.morningstar import MutualFundManagerInfo,MutualFundManagerDetail
from Service.common import convertStringToFloat,convertDateStringToInt



def fetchMutualFundDetailData():
    managerIds = MutualFundManagerInfo.objects.all().values('managerId','manager').distinct()
    print "total managerId length is: ", len(managerIds)
    for index in range(0, len(managerIds)):
        manager = managerIds[index]
        print "manager: ", manager
        managerId = manager["managerId"]
        managerName = manager["manager"]
        print "manager id: ", managerId
        fetchMutualFundEachData(managerId, managerName)
    return {"msg":"ok"}

def fetchMutualFundEachData(managerId, managerName):
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    reqUrl = "https://cn2.morningstar.com/fundmanagers/managerhistory.aspx?managerid=" + managerId
    print "reqUrl is:", reqUrl

    responseHtml = requestData(reqUrl)
    soup = BeautifulSoup(responseHtml.text, "lxml")
    # print responseHtml.text
    # print soup.prettify()

    resumTag = soup.find("div",class_="resum").get_text()


    targetTables = soup.findAll("table",class_="performance")
    print "targetTables length: ",len(targetTables)
    for ind in range(0,len(targetTables)):
        targetTable = targetTables[ind]
        # print "targetTable:",targetTable
        trs = targetTable.findAll('tr')
        for index in range(1,len(trs)):
            tr = trs[index]
            tds = tr.findAll('td')
            print "len: ", len(tds)

            code = tds[0].find("a").get_text()

            newMutualFundManagerDetail = MutualFundManagerDetail.objects.filter(code=code, managerId=managerId)
            if newMutualFundManagerDetail :
                newMutualFundManagerDetail = newMutualFundManagerDetail[0]
                print "get MutualFundManagerDetail saved info is: ", MutualFundManagerDetail
            else:
                print "get MutualFundManagerDetail saved info is null, create new one.code:",code
                newMutualFundManagerDetail = MutualFundManagerDetail(code=code, managerId=managerId)

            i = 1
            newMutualFundManagerDetail.name = tds[i].find("a").get_text()
            i += 1
            newMutualFundManagerDetail.manageStart = tds[i].get_text()
            #转换日期到Date
            newMutualFundManagerDetail.manageStartDate = newMutualFundManagerDetail.manageStart
            i += 1
            newMutualFundManagerDetail.manageEnd = tds[i].get_text()
            if newMutualFundManagerDetail.manageEnd == '-' or newMutualFundManagerDetail.manageEnd == '' or newMutualFundManagerDetail.manageEnd == ' ':
                newMutualFundManagerDetail.onPosition = 1
            else:
                newMutualFundManagerDetail.onPosition = 0
                #转换日期到Date
                newMutualFundManagerDetail.manageEndDate = newMutualFundManagerDetail.manageEnd
            i += 1
            newMutualFundManagerDetail.length = convertDateStringToInt(tds[i].get_text())
            i += 1
            newMutualFundManagerDetail.manageAchive = convertStringToFloat(tds[i].get_text())
            i += 1
            newMutualFundManagerDetail.manageAvgAchive = convertStringToFloat(tds[i].get_text())
            newMutualFundManagerDetail.updateDate = date
            newMutualFundManagerDetail.manager = managerName
            newMutualFundManagerDetail.resum = resumTag
            newMutualFundManagerDetail.save()

def requestData(reqUrl):
    responseHtml = requests.get(reqUrl)

    return responseHtml

# fetchMutualFundBuyData()