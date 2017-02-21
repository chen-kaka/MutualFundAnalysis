# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Item, Field

# class MutualfundscrachItem(Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class TencentItem(Item):
    name = Field()                # 职位名称
    catalog = Field()             # 职位类别
    workLocation = Field()        # 工作地点
    recruitNumber = Field()       # 招聘人数
    detailLink = Field()          # 职位详情页链接
    publishTime = Field()         # 发布时间

class MutualFundRatingItem(Item):
    code = Field()                # 基金代码
    name = Field()                # 基金名称
    nav = Field()                 # 单位净值
    StarRating3 = Field()         # 晨星三年评级
    StarRating5 = Field()         # 晨星五年评级
    SD3Year = Field()             # 三年波动幅度
    SD3YearComment = Field()      # 三年波动幅度评价
    DR3Year = Field()             # 三年晨星风险系数
    DR3YearComment = Field()      # 三年晨星风险系数评价
    SR3Year = Field()             # 三年夏普比例
    SR3YearComment = Field()      # 三年夏普比例评价
    ReturnYTD = Field()           # 今年总回报率
    ranking = Field()             # 排名