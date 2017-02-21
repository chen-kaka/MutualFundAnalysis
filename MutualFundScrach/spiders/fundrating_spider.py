# -*- coding: utf-8 -*-

import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from MutualFundScrach.items import *
from MutualFundScrach.misc.log import *


class TencentSpider(CrawlSpider):
    name = "mutualfund-rating"
    allowed_domains = ["morningstar.com"]
    start_urls = [
        "https://cn2.morningstar.com/handler/fundranking.ashx?date=2017-02-17&fund=&category=stock&rating=&company=&cust=&sort=ReturnYTD&direction=desc&tabindex=0&pageindex=1&pagesize=20" #&randomid=0.8141852494074107
    ]
    rules = [ # 定义爬取URL的规则
        Rule(sle(allow=("/position.php\?&start=\d{,4}#a")), follow=True, callback='parse_item')
    ]

    def parse_item(self, response): # 提取数据到Items里面，主要用到XPath和CSS选择器提取网页数据
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        sites_even = sel.css('table.fr_tablecontent tr.even')
        for site in sites_even:
            item = MutualFundRatingItem()

            index = 1
            item['code'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['name'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['nav'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['StarRating3'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['StarRating5'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['SD3Year'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['SD3YearComment'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['DR3Year'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['DR3YearComment'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['SR3Year'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['SR3YearComment'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['ReturnYTD'] = site.css('tr > td:nth-child('+index+')::text').extract()
            index += 1
            item['ranking'] = site.css('tr > td:nth-child('+index+')::text').extract()
            items.append(item)

        info('parsed ' + str(response))
        return items


    def _process_request(self, request):
        info('process ' + str(request))
        return request