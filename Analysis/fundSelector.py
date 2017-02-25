# -*- coding: utf-8 -*-

from Model.fundselector import FundRecommend
from Model.morningstar import MutualFundManagerInfo,MutualFundManagerDetail,MutualFundReturnInfo,MutualFundBuyInfo,MutualFundRating

def selectFund():
    #筛选出所有基金经理管理期业绩好于管理期同类平均业绩的基金
    betterThanAvgsFunds = MutualFundManagerDetail.objects.filter(manageAchive >= manageAvgAchive )

    print 'betterThanAvgsFunds length is: ', len(betterThanAvgsFunds)
    #过滤掉所有非"开放"的基金

    #同时1年,2年,3年,5年回报都得大于等于0,且设立以来的回报都要大于0

    #过滤掉基金评级在1,2级的基金

    #查询出这些基金的 三年标准差、 三年晨星风险系数、 三年夏普比例

    # 根据 三年夏普比例 由高到低排序

    # 根据 三年晨星风险系数 由小到大排序

    #获取每个查询集合的前20名

    # 根据 三年标准差 由小到大排序