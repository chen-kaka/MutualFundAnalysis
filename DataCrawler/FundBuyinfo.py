# -*- coding: utf-8 -*-

import time
import requests
import traceback
from bs4 import BeautifulSoup
from Model.morningstar import MutualFundBuyInfo
from Service.common import convertStringToFloatQoutExclude

def pagingFetchMutualFundBuyData():
    try:
        pagesize = 50
        totalCount = fetchMutualFundBuyData(1)

        reqPages = totalCount / pagesize + 1
        print "req total pages: ", reqPages
        for index in range(1, reqPages):
            fetchMutualFundBuyData(index+1)
        return {"msg":"ok"}
    except:
        traceback.print_exc()
        return {"msg":"fetch error."}

def fetchMutualFundBuyData(page):
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    reqUrl = "http://cn2.morningstar.com/quickrank/default.aspx"
    print "reqUrl is:", reqUrl, ", requesting page: ", page

    #lbOperations, AspNetPager1

    data = {
        "__EVENTTARGET":"ctl00$cphMain$AspNetPager1",
        "__EVENTARGUMENT":1,
        "__LASTFOCUS":"",
        "__VIEWSTATE":"/wEPDwUKMTI2NDQ3NTQ1NQ8WBh4KQ3VycmVudFRhYgUKb3BlcmF0aW9ucx4JU29ydEZpbGVkBQpTdGFyUmF0aW5nHgdTb3J0RGlyBQRERVNDFgJmD2QWAgIDD2QWAmYPZBYYAgEPDxYCHgRUZXh0BRnor4Tnuqfml6XmnJ/vvJoyMDE3LTA5LTMwZGQCAg8PFgQfAwUa5p+l55yL5pyA6L+R5pyI5pyr6K+E57qnPj4eB1Zpc2libGVnZGQCBw8QDxYGHg1EYXRhVGV4dEZpZWxkBQROYW1lHg5EYXRhVmFsdWVGaWVsZAUCSWQeC18hRGF0YUJvdW5kZ2QQFYEBEC0t5Z+66YeR5YWs5Y+4LS0k5a6J5L+h5Z+66YeR566h55CG5pyJ6ZmQ6LSj5Lu75YWs5Y+4HuWuneebiOWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTljJfkv6HnkZ7kuLDln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Y2a5pe25Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4Kua4pOa1t+axh+mHkeivgeWIuOi1hOS6p+euoeeQhuaciemZkOWFrOWPuB7otKLpgJrln7rph5HnrqHnkIbmnInpmZDlhazlj7ge6LSi6YCa6K+B5Yi45pyJ6ZmQ6LSj5Lu75YWs5Y+4HumVv+WuieWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7plb/ln47ln7rph5HnrqHnkIbmnInpmZDlhazlj7ge6ZW/5rGf6K+B5Yi46IKh5Lu95pyJ6ZmQ5YWs5Y+4HumVv+ebm+WfuumHkeeuoeeQhuaciemZkOWFrOWPuCTplb/kv6Hln7rph5HnrqHnkIbmnInpmZDotKPku7vlhazlj7gY5Yib6YeR5ZCI5L+h5Z+66YeR5YWs5Y+4HuWkp+aIkOWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lvrfpgqbln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Lic5pa55Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuS4nOaWueivgeWIuOiCoeS7veaciemZkOWFrOWPuCTkuJzmtbfln7rph5HnrqHnkIbmnInpmZDotKPku7vlhazlj7ge5Lic5ZC05Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuS4nOWFtOivgeWIuOiCoeS7veaciemZkOWFrOWPuCTmlrnmraPlr4zpgqbln7rph5HnrqHnkIbmnInpmZDlhazlj7gh5a+M5a6J6L6+5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWvjOWbveWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lr4zojaPln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5qC85p6X5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOW3pemTtueRnuS/oeWfuumHkeeuoeeQhuaciemZkOWFrOWPuCflhYnlpKfkv53lvrfkv6Hln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5bm/5Y+R5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWbvemDveivgeWIuOiCoeS7veaciemZkOWFrOWPuCrlm73mtbflr4zlhbDlhYvmnpfln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Zu96YeR5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4KuWbveW8gOazsOWvjOWfuumHkeeuoeeQhuaciemZkOi0o+S7u+WFrOWPuCHlm73ogZTlronln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5Zu95a+/5a6J5L+d5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWbveazsOWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTlm73mipXnkZ7pk7bln7rph5HnrqHnkIbmnInpmZDlhazlj7gh5rW35a+M6YCa5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOaBkueUn+WJjea1t+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7mgZLnlJ/mipXotYTnrqHnkIbmnInpmZDlhazlj7gk57qi5aGU57qi5Zyf5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOe6ouWcn+WIm+aWsOWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7ms5Plvrfln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Y2O5a6J5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWNjuWuneWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTljY7lrrjmnKrmnaXln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Y2O5a+M5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWNjuiejeivgeWIuOiCoeS7veaciemZkOWFrOWPuCTljY7mtqblhYPlpKfln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Y2O5ZWG5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOWNjuazsOafj+eRnuWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTljY7ms7Dkv53lhbTln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Y2O5rOw6K+B5Yi46IKh5Lu95pyJ6ZmQ5YWs5Y+4HuWNjuWkj+WfuumHkeeuoeeQhuaciemZkOWFrOWPuCTmsYflronln7rph5HnrqHnkIbmnInpmZDotKPku7vlhazlj7gk5rGH5Liw5pmL5L+h5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4J+axh+a3u+WvjOWfuumHkeeuoeeQhuiCoeS7veaciemZkOWFrOWPuB7lmInlkIjln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5ZiJ5a6e5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOW7uuS/oeWfuumHkeeuoeeQhuaciemZkOi0o+S7u+WFrOWPuCTlu7rpk7blm73pmYXotYTkuqfnrqHnkIbmnInpmZDlhazlj7ge5rGf5L+h5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4J+S6pOmTtuaWvee9l+W+t+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7ph5Hkv6Hln7rph5HnrqHnkIbmnInpmZDlhazlj7ge6YeR6bmw5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOmHkeWFg+mhuuWuieWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTmma/pobrplb/ln47ln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Lmd5rOw5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOawkeeUn+WKoOmTtuWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTmkanmoLnln7rph5HvvIjkuprmtLLvvInmnInpmZDlhazlj7gt5pGp5qC55aOr5Li55Yip5Y2O6ZGr5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWNl+aWueWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7ljZfljY7l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HwMFD+S4mue7qeWSjOmjjumZqR8IZR8JAgJkZAIODw8WBh8DBQzmipXotYTnu4TlkIgfCGUfCQICZGQCDw8PFgYfAwUM6LSt5Lmw5L+h5oGvHwgFBmFjdGl2ZR8JAgJkZAISDw8WAh8DBQQ3MDUzZGQCEw8PFgQeC1JlY29yZGNvdW50Ao03HghQYWdlU2l6ZQIZZGQCFA8QZGQWAWZkGAIFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYxBR1jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmckMAUdY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nJDEFHWN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZyQyBR1jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmckMwUdY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nJDQFHWN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZyQ1BR1jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmckNQUeY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nNSQwBR5jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmc1JDEFHmN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZzUkMgUeY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nNSQzBR5jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmc1JDQFHmN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZzUkNQUeY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nNSQ1BRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDAFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkMQUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQyBRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDMFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkNAUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQ1BRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDYFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkNwUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQ4BRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDgFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkMAUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxBRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDIFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkMwUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQ0BRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDUFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkNgUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQ3BRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDgFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkOQUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMAUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMQUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMgUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMwUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxNAUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxNQUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxNgUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxNwUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxOAUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxOAUYY3RsMDAkY3BoTWFpbiRjYmxMZXZlbCQwBRhjdGwwMCRjcGhNYWluJGNibExldmVsJDEFGGN0bDAwJGNwaE1haW4kY2JsTGV2ZWwkMgUYY3RsMDAkY3BoTWFpbiRjYmxMZXZlbCQzBRhjdGwwMCRjcGhNYWluJGNibExldmVsJDMFGGN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdA88KwAKAQgCAWTSJ9+GwyNgox84MLH3bEfiI02ZWg==",
        "__EVENTVALIDATION":"/wEWvAEC6aK5/gkCn7zM0gcCoLzM0gcCnbzM0gcCnrzM0gcCo7zM0gcCpLzM0gcCs7y4qQoCs7y0qQoCs7zAqQoCs7y8qQoCs7zIqQoCs7zEqQoC7PrGyggC7PrapQEC7PrugAoC7PqC3AIC7Pr23QUC7PqKuQ4C7PqelAcC7Pqy7w8C7Prmow4CqvnIgwECxeLmmAsC9KaN2QwCj5Cr7gYClp7A2AkCsYfe7QMC4MuErgUC+7Siww8CgsO3rQICnazVwgwCxeKmywYCxeK6pg8CxeLOgQgCxeLiXALF4va3CQLF4oqTAgLF4p7uCgLF4rLJAwLF4sakDALF4OKECgLF4M6pAQLF4Iq7CwLF4PbfAgKFtqecDQKgmNKlBgKoiqG4AwKpipm4AwLNk4OlBQLDk4ulBQLCk4ulBQKhmNqlBgLI0q2MBwLt+5O5CQLw3/HlBALs+4e5CQLL0qWMBwLJ0rmMBwLEoeDTCALI0qGMBwLnuP3SDwKpiuW4AwKV5aOTCQKgmKKmBgK6oYTTCALnuO3SDwKpiqm4AwLI0rGMBwLkuOnSDwKuiqm4AwLt+5u5CQLy36XmBAKgmKqmBgLkuPHSDwLL0p2MBwLnuOHSDwLz36HmBALnuOnSDwLCk8elBQKU5aOTCQLz3/nlBALNk/ulBQK6obDTCALftpr4AgLI0p2MBwKhmKKmBgLftuL4AgLCk5OlBQLmuN3SDwKpiqG4AwLnuPnSDwKhmKqmBgLI0qWMBwLI0rmMBwKgmKamBgLJ0qmMBwLJ0q2MBwKjmIqmBgLDk5elBQLCk+elBQLL0pmMBwLi+5u5CQKpioW4AwLmuOXSDwLftpL4AgKU5YeTCQKU5dOSCQLDk5OlBQLFoYzTCALz3/3lBALFoYDTCAKuirm4AwLnuPXSDwLw3/nlBAKpirm4AwLmuNnSDwLkuO3SDwLFobjTCALetuL4AgKU5aeTCQLI0r2MBwLw3/XlBAKU5deSCQLEoajTCALets74AgLt+5+5CQKhmK6mBgLZts74AgLFoeDTCALFoYTTCAK6obTTCALt+/+5CQLs+4O5CQLJ0r2MBwKoipm4AwLetub4AgKoiuW4AwKU5duSCQLI0qmMBwKuirW4AwLCk5ulBQLJ0rGMBwKuir24AwKU5YOTCQKjmI6mBgKX5YeTCQKjmNalBgLetsL4AgLnuN3SDwLw3/3lBALZtsL4AgKpir24AwLs+/+5CQLCk5+lBQKU5c+SCQKgmI6mBgLz36XmBALy36HmBALFobDTCALDk+elBQLi+4+5CQLnuPHSDwLi+4u5CQKgmIqmBgLw38HlBALi+5e5CQLz38XlBAKhmNKlBgLt+/u5CQLkuPXSDwKpirG4AwK6obzTCALNk8elBQKEiMLTDAKEiMLTDAKQ18zyAwKQ18zyAwLF7Je2DgKvw/+HAQKWjpmUAwLdt+TKBQL10KDSBgL+xcmpAQL79sCsAQL1mZbBDQLwmarBDQL04uizCg2tOiRnu7ae6/hDhmegjXInKh6g",
        "ctl00$cphMain$ddlCompany":"",
        "ctl00$cphMain$ddlPortfolio":"",
        "ctl00$cphMain$ddlWatchList":"",
        "ctl00$cphMain$txtFund":"基金名称",
        "ctl00$cphMain$ddlPageSite":50
    }
    data["__EVENTARGUMENT"] = page

    responseHtml = requestData(reqUrl, data)
    soup = BeautifulSoup(responseHtml.text, "lxml")
    # print responseHtml.text
    # print soup.prettify()

    summaryData = soup.find(id='ctl00_cphMain_TotalResultLabel')
    # print "summaryData: ",summaryData
    if summaryData == None or any(summaryData) == False :
        print "fetch fund buyinfo data error. exit."
        return 0
    totalCount =int(summaryData.get_text())
    print "totalCount: ",totalCount

    targetTable = soup.find(id="ctl00_cphMain_gridResult")
    trs = targetTable.findAll('tr')
    for index in range(1,len(trs)):
        tr = trs[index]
        tds = tr.findAll('td')
        print "len: ", len(tds)
        print "tds: ",tds
        code = tds[2].find("a").get_text()

        newMutualFundBuyInfo = MutualFundBuyInfo.objects.filter(code=code)
        if newMutualFundBuyInfo :
            newMutualFundBuyInfo = newMutualFundBuyInfo[0]
            print "get MutualFundBuyInfo saved info is: ", MutualFundBuyInfo
        else:
            print "get MutualFundBuyInfo saved info is null, create new one."
            newMutualFundBuyInfo = MutualFundBuyInfo(code=code)

        i = 3
        newMutualFundBuyInfo.name = tds[i].find("a").get_text()
        print "code:",code,"name:",newMutualFundBuyInfo.name
        i += 1
        newMutualFundBuyInfo.establishDate = tds[i].get_text()
        i += 1
        newMutualFundBuyInfo.applyState = tds[i].get_text()
        i += 1
        newMutualFundBuyInfo.returnState = tds[i].get_text()
        i += 1
        newMutualFundBuyInfo.minBuy = convertStringToFloatQoutExclude(tds[i].get_text())
        print "newMutualFundBuyInfo.minBuy:",newMutualFundBuyInfo.minBuy
        i += 1
        newMutualFundBuyInfo.frontCharge = convertStringToFloatQoutExclude(tds[i].get_text())
        i += 1
        newMutualFundBuyInfo.backCharge = convertStringToFloatQoutExclude(tds[i].get_text())
        i += 1
        newMutualFundBuyInfo.redeemFee = convertStringToFloatQoutExclude(tds[i].get_text())
        i += 1
        newMutualFundBuyInfo.manageFee = convertStringToFloatQoutExclude(tds[i].get_text())
        i += 1
        newMutualFundBuyInfo.trusteeFee = convertStringToFloatQoutExclude(tds[i].get_text())
        i += 1
        newMutualFundBuyInfo.serviceFee = convertStringToFloatQoutExclude(tds[i].get_text())
        newMutualFundBuyInfo.updateDate = date
        print "newMutualFundBuyInfo is:",newMutualFundBuyInfo
        newMutualFundBuyInfo.save()
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
        "Cookie":"Cookie:BAIDU_SSP_lcr=https://www.baidu.com/link?url=qXDBs04d3uhjRer7II5sR53HLoM6-8awY6h4ftfbcPSJ0TDc-9NAK1gSM1KiXBGU5pxXXQf5EwvijnS0kwzQua&wd=&eqid=9d5ed8850002e19e000000035a07cbe4; ASP.NET_SessionId=dw5brkflfvroes55sxle2155; MS_LocalEmailAddr=chen-kaka@163.com=; user=username=chen-kaka@163.com&nickname=&status=&password=; BIGipServercn=2241287690.20480.0000; Hm_lvt_eca85e284f8b74d1200a42c9faa85464=1510459525; Hm_lpvt_eca85e284f8b74d1200a42c9faa85464=1510471903; __utmt=1; __utma=172984700.1666955223.1510459530.1510467618.1510471908.4; __utmb=172984700.1.10.1510471908; __utmc=172984700; __utmz=172984700.1510460404.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic"
    }
    responseHtml = requests.post(reqUrl, data=payload, headers=headers)

    return responseHtml

# fetchMutualFundBuyData()