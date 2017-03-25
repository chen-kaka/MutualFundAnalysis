# -*- coding: utf-8 -*-

from Model.fundselector import FundRecommend
from django.core import serializers

# 数据库操作
def getRecommendList():
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = FundRecommend.objects.all()
    retResp = serializers.serialize('json', list)
    return retResp