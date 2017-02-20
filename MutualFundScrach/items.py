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