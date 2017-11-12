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
        "__VIEWSTATE":"/wEPDwUJLTc0ODYyMjI5DxYGHgpDdXJyZW50VGFiBQpvcGVyYXRpb25zHglTb3J0RmlsZWQFClN0YXJSYXRpbmceB1NvcnREaXIFBERFU0MWAmYPZBYCAgMPZBYCZg9kFhgCAQ8PFgIeBFRleHQFGeivhOe6p+aXpeacn++8mjIwMTYtMTItMzFkZAICDw8WBB8DBRrmn6XnnIvmnIDov5HmnIjmnKvor4Tnuqc+Ph4HVmlzaWJsZWdkZAIHDxAPFgYeDURhdGFUZXh0RmllbGQFBE5hbWUeDkRhdGFWYWx1ZUZpZWxkBQJJZB4LXyFEYXRhQm91bmRnZBAVeRAtLeWfuumHkeWFrOWPuC0tJOWuieS/oeWfuumHkeeuoeeQhuaciemZkOi0o+S7u+WFrOWPuB7lrp3nm4jln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5YyX5L+h55Ge5Liw5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWNmuaXtuWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7otKLpgJrln7rph5HnrqHnkIbmnInpmZDlhazlj7ge6LSi6YCa6K+B5Yi45pyJ6ZmQ6LSj5Lu75YWs5Y+4HumVv+WuieWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7plb/ln47ln7rph5HnrqHnkIbmnInpmZDlhazlj7ge6ZW/5rGf6K+B5Yi46IKh5Lu95pyJ6ZmQ5YWs5Y+4HumVv+ebm+WfuumHkeeuoeeQhuaciemZkOWFrOWPuCTplb/kv6Hln7rph5HnrqHnkIbmnInpmZDotKPku7vlhazlj7gY5Yib6YeR5ZCI5L+h5Z+66YeR5YWs5Y+4HuWkp+aIkOWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lvrfpgqbln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Lic5pa55Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuS4nOaWueivgeWIuOiCoeS7veaciemZkOWFrOWPuCTkuJzmtbfln7rph5HnrqHnkIbmnInpmZDotKPku7vlhazlj7ge5Lic5ZC05Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuS4nOWFtOivgeWIuOiCoeS7veaciemZkOWFrOWPuCTmlrnmraPlr4zpgqbln7rph5HnrqHnkIbmnInpmZDlhazlj7gh5a+M5a6J6L6+5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWvjOWbveWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lr4zojaPln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5bel6ZO255Ge5L+h5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4J+WFieWkp+S/neW+t+S/oeWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lub/lj5Hln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5bm/5Y+R6K+B5Yi46IKh5Lu95pyJ6ZmQ5YWs5Y+4HuWbvemDveivgeWIuOiCoeS7veaciemZkOWFrOWPuCrlm73mtbflr4zlhbDlhYvmnpfln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Zu96YeR5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4KuWbveW8gOazsOWvjOWfuumHkeeuoeeQhuaciemZkOi0o+S7u+WFrOWPuCHlm73ogZTlronln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5Zu95a+/5a6J5L+d5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWbveazsOWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTlm73mipXnkZ7pk7bln7rph5HnrqHnkIbmnInpmZDlhazlj7gh5rW35a+M6YCa5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuaBkueUn+aKlei1hOeuoeeQhuaciemZkOWFrOWPuCTnuqLloZTnuqLlnJ/ln7rph5HnrqHnkIbmnInpmZDlhazlj7gk57qi5Zyf5Yib5paw5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4Huazk+W+t+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7ljY7lronln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5Y2O5a6d5YW05Lia5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOWNjuWuuOacquadpeWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7ljY7lr4zln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Y2O6J6N6K+B5Yi46IKh5Lu95pyJ6ZmQ5YWs5Y+4JOWNjua2puWFg+Wkp+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7ljY7llYbln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5Y2O5rOw5p+P55Ge5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOWNjuazsOS/neWFtOWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7ljY7lpI/ln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5rGH5a6J5Z+66YeR566h55CG5pyJ6ZmQ6LSj5Lu75YWs5Y+4JOaxh+S4sOaZi+S/oeWfuumHkeeuoeeQhuaciemZkOWFrOWPuCfmsYfmt7vlr4zln7rph5HnrqHnkIbogqHku73mnInpmZDlhazlj7ge5ZiJ5ZCI5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWYieWunuWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTlu7rkv6Hln7rph5HnrqHnkIbmnInpmZDotKPku7vlhazlj7ge5rGf5L+h5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4J+S6pOmTtuaWvee9l+W+t+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7ph5Hkv6Hln7rph5HnrqHnkIbmnInpmZDlhazlj7ge6YeR6bmw5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOmHkeWFg+mhuuWuieWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTmma/pobrplb/ln47ln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Lmd5rOw5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOawkeeUn+WKoOmTtuWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTmkanmoLnln7rph5HvvIjkuprmtLLvvInmnInpmZDlhazlj7gt5pGp5qC55aOr5Li55Yip5Y2O6ZGr5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWNl+aWueWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTlhpzpk7bmsYfnkIbln7rph5HnrqHnkIbmnInpmZDlhazlj7ge6K+65a6J5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuivuuW+t+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7puY/ljY7ln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5bmz5a6J5aSn5Y2O5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOa1pumTtuWuieebm+WfuumHkeeuoeeQhuaciemZkOWFrOWPuCTliY3mtbflvIDmupDln7rph5HnrqHnkIbmnInpmZDlhazlj7ge6J6N6YCa5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4DOWxseilv+ivgeWIuCTkuIrmipXmkanmoLnln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5LiK6ZO25Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOeUs+S4h+iPseS/oeWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lpKrlubPln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5rOw6L6+5a6P5Yip5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOazsOW6t+i1hOS6p+euoeeQhuaciemZkOi0o+S7u+WFrOWPuB7ms7Dkv6Hln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5aSp5byY5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuWkqeayu+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7kuIflrrbln7rph5HnrqHnkIbmnInpmZDlhazlj7ge6KW/6YOo5Yip5b6X5Z+66YeR566h55CG5YWs5Y+4HuWFiOmUi+WfuumHkeeuoeeQhuaciemZkOWFrOWPuCTmlrDljY7ln7rph5HnrqHnkIbogqHku73mnInpmZDlhazlj7gq5paw55aG5YmN5rW36IGU5ZCI5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuaWsOayg+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7pkavlhYPln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5L+h6K+a5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOS/oei+vua+s+mTtuWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7lhbTlhajln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5YW05Lia5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4JOWFtOmTtuWfuumHkeeuoeeQhuaciemZkOi0o+S7u+WFrOWPuB7ooYzlgaXotYTkuqfnrqHnkIbmnInpmZDlhazlj7gh5piT5pa56L6+5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuebiuawkeWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7pk7bmsrPln7rph5HnrqHnkIbmnInpmZDlhazlj7ge6ZO25Y2O5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuiLseWkp+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7msLjotaLln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5ZyG5L+h5rC45Liw5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuaLm+WVhuWfuumHkeeuoeeQhuaciemZkOWFrOWPuB7mtZnllYbln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5rWZ5ZWG6K+B5Yi45pyJ6ZmQ6LSj5Lu75YWs5Y+4HuS4rea1t+WfuumHkeeuoeeQhuaciemZkOWFrOWPuB7kuK3oiKrln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Lit5Yqg5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuS4remHkeWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTkuK3np5HmsoPlnJ/ln7rph5HnrqHnkIbmnInpmZDlhazlj7ge5Lit5qyn5Z+66YeR566h55CG5pyJ6ZmQ5YWs5Y+4HuS4reiejeWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTkuK3kv6Hlu7rmipXln7rph5HnrqHnkIbmnInpmZDlhazlj7gk5Lit6ZO25Zu96ZmF6K+B5Yi45pyJ6ZmQ6LSj5Lu75YWs5Y+4HuS4remTtuWfuumHkeeuoeeQhuaciemZkOWFrOWPuCTkuK3pk7bpppnmuK/otYTkuqfnrqHnkIbmnInpmZDlhazlj7gq5Lit6YKu5Yib5Lia5Z+66YeR566h55CG6IKh5Lu95pyJ6ZmQ5YWs5Y+4FXkAAzU2MAM0NzUDNTk1AzQ3NgM1NTYDNjQwAzU1OAM1MjkDNjQzAzQ3OQM0NzgDNjA4AzQ5MQM1NjgDNTE3AzU4NQM2MDQDNTIwAzYyMQM1NTcDNTU1AzUyOAM2NDcDNTA5AzQ5MwM1MDADNjQ0AzYyNwM0OTgDNTY3AzU4MwM1NDcDNTg2AzUwNAM1MjMDNDk2AzYzMgM1OTgDNjIwAzYxMgM1MzYDNDk3AzU3NQM1MDcDNjAwAzU3OAM1MDgDNTMwAzY0OAM0ODADNjQ2AzUwNgM0ODgDNjA5AzUwNQM0NzcDNTk0AzU0NAM2MzYDNTAxAzUzMwM1MTEDNjE1AzUzNwM2MjMDNTE1AzQ4NwM1MzEDNTEyAzUxNAM1MTgDNTU0AzQ3MQM1ODIDNTE5AzYxMAM0ODIDNTkxAzUyMQM1OTkDNDY5AzYxOAM0OTUDNTIyAzQ4NQM1MjQDNTQ4AzY0NQM1MTYDNjI4AzYyNQM1ODQDNDkwAzQ5NAM0NzADNTkyAzU5NwM2MzMDNDkyAzUyNQM0OTkDNTI2AzU3NAM1OTADNTkzAzQ4MwM1NTEDNjA2AzUyNwM2NDkDNTgwAzYwMwM2MzkDNTEzAzYxMQM1ODkDNjM3AzUzNQM2NDEDNDg2FCsDeWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIIDxBkEBUCEC0t5oqV6LWE57uE5ZCILS0P55m75b2V5ZCO5Y+v55SoFQIAABQrAwJnZ2RkAgkPEGQQFQIQLS3op4Llr5/liJfooagtLQ/nmbvlvZXlkI7lj6/nlKgVAgAAFCsDAmdnZGQCDA8PFgYfAwUG5b+r54WnHghDc3NDbGFzc2UeBF8hU0ICAmRkAg0PDxYGHwMFD+S4mue7qeWSjOmjjumZqR8IZR8JAgJkZAIODw8WBh8DBQzmipXotYTnu4TlkIgfCGUfCQICZGQCDw8PFgYfAwUM6LSt5Lmw5L+h5oGvHwgFBmFjdGl2ZR8JAgJkZAISDw8WAh8DBQQ2MDYyZGQCEw8PFgYeC1JlY29yZGNvdW50Aq4vHghQYWdlU2l6ZQIZHhBDdXJyZW50UGFnZUluZGV4AgFkZAIUDxBkZBYBZmQYAgUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFkYFHWN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZyQwBR1jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmckMQUdY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nJDIFHWN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZyQzBR1jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmckNAUdY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nJDUFHWN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZyQ1BR5jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmc1JDAFHmN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZzUkMQUeY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nNSQyBR5jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmc1JDMFHmN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZzUkNAUeY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nNSQ1BR5jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmc1JDUFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkMAUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQxBRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDIFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkMwUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQ0BRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDUFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkNgUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQ3BRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDgFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkOAUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQwBRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDEFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkMgUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQzBRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDQFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkNQUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQ2BRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDcFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkOAUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQ5BRxjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDEwBRxjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDExBRxjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDEyBRxjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDEzBRxjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDE0BRxjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDE0BRhjdGwwMCRjcGhNYWluJGNibExldmVsJDAFGGN0bDAwJGNwaE1haW4kY2JsTGV2ZWwkMQUYY3RsMDAkY3BoTWFpbiRjYmxMZXZlbCQyBRhjdGwwMCRjcGhNYWluJGNibExldmVsJDMFGGN0bDAwJGNwaE1haW4kY2JsTGV2ZWwkMwUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDAyJGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwwMyRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMDQkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDA1JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwwNiRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMDckY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDA4JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwwOSRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMTAkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDExJGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwxMiRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMTMkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDE0JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwxNSRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMTYkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDE3JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwxOCRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMTkkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDIwJGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwyMSRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMjIkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDIzJGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwyNCRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMjUkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDI2JGNoa0Z1bmQFGGN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdA88KwAKAQgCAWSuUZ2e4m7f1hQSTWyWid2XEtY3TA==",
        "__EVENTVALIDATION":"/wEW1QECy93nrgICn7zM0gcCoLzM0gcCnbzM0gcCnrzM0gcCo7zM0gcCpLzM0gcCs7y4qQoCs7y0qQoCs7zAqQoCs7y8qQoCs7zIqQoCs7zEqQoC7PrGyggC7PrapQEC7PrugAoC7PqC3AIC7Pr23QUC7PqKuQ4C7PqelAcC7Pqy7w8C7Prmow4CqvnIgwECxeLmmAsC9KaN2QwCj5Cr7gYClp7A2AkCsYfe7QMC4MuErgUC+7Siww8CgsO3rQICnazVwgwCxeKmywYCxeK6pg8CxeLOgQgCxeLiXALF4va3CQLF4OKECgLF4M6pAQLF4Iq7CwLF4PbfAgKFtqecDQKgmNKlBgKoiqG4AwKpipm4AwLNk4OlBQLCk4ulBQKhmNqlBgLI0q2MBwLt+5O5CQLw3/HlBALs+4e5CQLL0qWMBwLJ0rmMBwLEoeDTCALI0qGMBwLnuP3SDwKpiuW4AwKV5aOTCQKgmKKmBgK6oYTTCALnuO3SDwKpiqm4AwLI0rGMBwLkuOnSDwLt+5u5CQLy36XmBAKgmKqmBgKV5dOSCQLkuPHSDwLL0p2MBwLnuOHSDwLz36HmBALnuOnSDwLCk8elBQKU5aOTCQLz3/nlBALNk/ulBQLftpr4AgLI0p2MBwKhmKKmBgLftuL4AgLCk5OlBQLmuN3SDwKpiqG4AwLnuPnSDwKhmKqmBgLI0qWMBwLI0rmMBwKgmKamBgLJ0qmMBwKjmIqmBgLDk5elBQLCk+elBQLL0pmMBwLi+5u5CQKpioW4AwLmuOXSDwKU5YeTCQKU5dOSCQLDk5OlBQLFoYzTCALz3/3lBALFoYDTCAKuirm4AwLnuPXSDwLw3/nlBAKpirm4AwLmuNnSDwLFobjTCALetuL4AgKU5aeTCQLI0r2MBwKU5deSCQLEoajTCALets74AgLt+5+5CQKhmK6mBgLZts74AgLFoeDTCALFoYTTCALt+/+5CQLs+4O5CQLJ0r2MBwKoipm4AwLetub4AgKoiuW4AwKU5duSCQLI0qmMBwKuirW4AwLCk5ulBQLJ0rGMBwKuir24AwKU5YOTCQKjmI6mBgKX5YeTCQKjmNalBgLetsL4AgLnuN3SDwLw3/3lBALZtsL4AgKpir24AwLs+/+5CQLCk5+lBQKU5c+SCQKgmI6mBgLz36XmBALy36HmBALFobDTCALDk+elBQLnuPHSDwLi+4u5CQKgmIqmBgLw38HlBALi+5e5CQLz38XlBAK6oYDTCALt+/u5CQLkuPXSDwKpirG4AwK6obzTCALNk8elBQKEiMLTDAKEiMLTDAKQ18zyAwKQ18zyAwLF7Je2DgKvw/+HAQKWjpmUAwLdt+TKBQL10KDSBgL+xcmpAQKIv62ECAKe2tCSDwKLidTZDALdkbSPAwLytv6HDwLmnayICwL045YrAunA9p0DApzUw+sHApKgz+wDAq+skTYC9t601wUCytCYjQMCytD08AICytCQSQLK0IwrAsrQqJUCAsrQxPcBAsrQ4PgPAsrQ3NIPAt3cwNEBAt3cvLMBAt3cmI0DAt3c9PACAt3ckEkC3dyMKwLd3KiVAgLd3MT3AQLd3OD4DwLd3NzSDwLc5MDRAQLc5LyzAQLc5JiNAwLc5PTwAgLc5JBJAtzkjCsC3OSolQIC+/bArAEC9ZmWwQ0C8JmqwQ0C9OLoswo7zgzwsOYr5kz7/CEfAD6s+8XYHw==",
        "ctl00$cphMain$ddlCompany":"",
        "ctl00$cphMain$ddlPortfolio":"",
        "ctl00$cphMain$ddlWatchList":"",
        "ctl00$cphMain$txtFund":"基金名称",
        "ctl00$cphMain$ddlPageSite":"50"
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
        "Origin":"http://cn2.morningstar.com"
    }
    responseHtml = requests.post(reqUrl, data=payload, headers=headers)

    return responseHtml

# fetchMutualFundBuyData()