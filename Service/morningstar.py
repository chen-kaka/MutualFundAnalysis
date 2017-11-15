# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# 从首页先获取一次ViewState
def fetchFirstPageViewStateInfo():
    reqUrl = "http://cn2.morningstar.com/fundselect/default.aspx"
    print "reqUrl is:", reqUrl
    responseHtml = requestGetData(reqUrl)
    soup = BeautifulSoup(responseHtml.text, "lxml")
    # print soup.prettify()

    # 获取viewState
    viewStateData = soup.find(id='__VIEWSTATE')["value"]

    print "viewStateData: ", viewStateData

    return viewStateData


def requestGetData(reqUrl):
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Referer":"http://cn2.morningstar.com/quickrank/default.aspx",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Host":"cn2.morningstar.com",
        "Origin":"http://cn2.morningstar.com",
        "Cookie": "Cookie:BAIDU_SSP_lcr=https://www.baidu.com/link?url=qXDBs04d3uhjRer7II5sR53HLoM6-8awY6h4ftfbcPSJ0TDc-9NAK1gSM1KiXBGU5pxXXQf5EwvijnS0kwzQua&wd=&eqid=9d5ed8850002e19e000000035a07cbe4; ASP.NET_SessionId=dw5brkflfvroes55sxle2155; MS_LocalEmailAddr=chen-kaka@163.com=; user=username=chen-kaka@163.com&nickname=&status=&password=; BIGipServercn=2241287690.20480.0000; Hm_lvt_eca85e284f8b74d1200a42c9faa85464=1510459525; Hm_lpvt_eca85e284f8b74d1200a42c9faa85464=1510471903; __utmt=1; __utma=172984700.1666955223.1510459530.1510467618.1510471908.4; __utmb=172984700.1.10.1510471908; __utmc=172984700; __utmz=172984700.1510460404.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic"
    }
    responseHtml = requests.get(reqUrl, params={}, headers=headers)

    return responseHtml