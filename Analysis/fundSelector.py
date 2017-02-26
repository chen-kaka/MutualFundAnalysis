# -*- coding: utf-8 -*-

from django.db.models import F
from django.db.models import Q
from Model.fundselector import FundRecommend
from Model.morningstar import MutualFundManagerInfo,MutualFundManagerDetail,MutualFundReturnInfo,MutualFundBuyInfo,MutualFundRating

def selectFund():
    #筛选出所有基金经理管理期业绩好于管理期同类平均业绩的基金
    betterThanAvgsFunds = MutualFundManagerDetail.objects.filter(manageAchive__gte=F('manageAvgAchive'),onPosition=1)

    print 'betterThanAvgsFunds length is: ', len(betterThanAvgsFunds)
    #过滤掉所有非"开放"的基金
    openStateFunds = MutualFundBuyInfo.objects.filter(applyState='开放' , returnState='开放')
    print 'openStateFunds length is: ', len(openStateFunds)
    openStateFundsMap = convertListToMap(openStateFunds)
    returnInfoList = MutualFundReturnInfo.objects.filter(oneYearReturn__gte=0,
                                                         twoYearReturn__gte=0,
                                                         threeYearReturn__gte=0,
                                                         fiveYearReturn__gte=0)
    print 'returnInfoList length is: ', len(returnInfoList)
    returnInfoMap = convertListToMap(returnInfoList)
    fundRatingList = MutualFundRating.objects.filter(StarRating3__gte=2, StarRating5__gte=2)
    print 'fundRatingList length is: ', len(fundRatingList)
    fundRatingMap = convertListToMap(fundRatingList)
    passClosedFundSize = 0
    passAllUpZeroSize = 0
    passFundNotOneTwoSize = 0
    targetList = []
    for index in range(0, len(betterThanAvgsFunds)):
        considerItem = betterThanAvgsFunds[index]
        itemCode = considerItem.code

        if openStateFundsMap.has_key(itemCode) == False:
            continue
        passClosedFundSize += 1
        #同时1年,2年,3年,5年回报都得大于等于0,且设立以来的回报都要大于0
        if returnInfoMap.has_key(considerItem.code) == False:
            continue
        passAllUpZeroSize += 1
        #过滤掉基金评级在1,2级的基金
        if fundRatingMap.has_key(considerItem.code) == False:
            continue
        passFundNotOneTwoSize += 1
        #查询出这些基金的 三年标准差、 三年晨星风险系数、 三年夏普比例
        returnInfo = returnInfoMap.get(considerItem.code)
        threeYearStandard = returnInfo.threeYearStandard

        fundRatingInfo = fundRatingMap.get(considerItem.code)

        threeYearRisk = fundRatingInfo.DR3Year
        threeYearSharp = fundRatingInfo.SR3Year
        #三、五年评级
        StarRating3 = fundRatingInfo.StarRating3
        StarRating5 = fundRatingInfo.StarRating5

        considerItem.threeYearStandard = threeYearStandard
        considerItem.threeYearRisk = threeYearRisk
        considerItem.threeYearSharp = threeYearSharp
        considerItem.StarRating3 = StarRating3
        considerItem.StarRating5 = StarRating5
        targetList.append(considerItem)
    print 'passClosedFundSize:',passClosedFundSize, 'passAllUpZeroSize:',passAllUpZeroSize,'passFundNotOneTwoSize:',passFundNotOneTwoSize
    # 根据 三年夏普比例 由高到低排序
    sharpTargetList = sorted(targetList, key=lambda targetItem: targetItem.threeYearSharp, reverse=True)
    for i in range(0,10):
        print "code:",sharpTargetList[i].code,",name:",sharpTargetList[i].name,",threeYearSharp:",sharpTargetList[i].threeYearSharp
    # 根据 三年晨星风险系数 由小到大排序
    print "--------------------------------------------------"
    riskTargetList = sorted(targetList, key=lambda targetItem: targetItem.threeYearRisk)
    for i in range(0,10):
        print "code:",riskTargetList[i].code,",name:",riskTargetList[i].name,",threeYearRisk:",riskTargetList[i].threeYearRisk
    #获取每个查询集合的前30名中重叠的部分
    sharpTargetListLength = len(sharpTargetList)
    riskTargetListLength = len(riskTargetList)
    print "sharpTargetList length:",sharpTargetListLength,",and riskTargetList length:",riskTargetListLength
    riskTargetCodeMap = {}
    for i in range(0,50):
        riskTargetCodeMap[riskTargetList[i].code] = True
    bothExistedLists = []
    for i in range(0,50):
        if riskTargetCodeMap.has_key(sharpTargetList[i].code):
            bothExistedLists.append(sharpTargetList[i])
    print "bothExistedLists size is:",len(bothExistedLists),", bothExistedLists is:",bothExistedLists
    # 根据 三年标准差 由小到大排序
    standardTargetList = sorted(bothExistedLists, key=lambda targetItem: targetItem.threeYearStandard)
    for i in range(0,len(standardTargetList)):
        print "====final result: code:",standardTargetList[i].code,",name:",standardTargetList[i].name,\
            ",threeYearRisk:",standardTargetList[i].threeYearRisk,", threeYearSharp:",\
            standardTargetList[i].threeYearSharp,", threeYearStandard:",\
            standardTargetList[i].threeYearStandard,", StarRating3:", \
            standardTargetList[i].StarRating3,", StarRating5:", \
            standardTargetList[i].StarRating5
    print "total size:",len(standardTargetList)
    return {"ok":True}

def convertListToMap(list):
    map = {}
    for index in range(0, len(list)):
        item = list[index]
        code = item.code
        map[code] = item
    print "map:",len(map)
    return map