# -*- coding: utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup
from Model.morningstar import MutualFundReturnInfo
from Service.common import convertStringToFloat

def pagingFetchMutualFundReturnData():
    totalCount = fetchMutualFundReturnData()
    print "total totalCount: ", totalCount
    return {"msg":"ok"}

def fetchMutualFundReturnData():
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    reqUrl = "http://cn2.morningstar.com/fundselect/default.aspx"
    print "reqUrl is:", reqUrl

    #lbOperations, AspNetPager1

    data = {
        "__EVENTTARGET":"ctl00$cphMain$ddlPageSite",
        "__EVENTARGUMENT":"",
        "__LASTFOCUS":"",
        "__VIEWSTATE":"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NQM0OTkDNTI2AzU3NAM1OTADNTkzAzQ4MwM1NTEDNjA2AzUyNwM2NDkDNTgwAzYwMwM2MzkDNTEzAzYxMQM1ODkDNjM3AzUzNQM2NDEDNDg2FCsDeWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIODxAPFgYfAwUNUG9ydGZvbGlvTmFtZR8EBQtQb3J0Zm9saW9JZB8FZ2QQFQAVABQrAwBkZAIPDxAPFgYfAwUNV2F0Y2hMaXN0TmFtZR8EBQtXYXRjaExpc3RJZB8FZ2QQFQES5oiR55qE6Ieq6YCJ5Z+66YeRFQEBMBQrAwFnZGQCEg8PFgIeBFRleHQFGeivhOe6p+aXpeacn++8mjIwMTctMDEtMzFkZAIWDw8WBh8GBQblv6vnhaceCENzc0NsYXNzZR4EXyFTQgICZGQCFw8PFgYfBgUP5Lia57up5ZKM6aOO6ZmpHwcFBmFjdGl2ZR8IAgJkZAIYDw8WBh8GBQzmipXotYTnu4TlkIgfB2UfCAICZGQCGQ8PFgYfBgUM6LSt5Lmw5L+h5oGvHwdlHwgCAmRkAhwPDxYCHwYFBDYwNzdkZAIdDw8WBB4LUmVjb3JkY291bnQCvS8eCFBhZ2VTaXplAhlkZAIeDxBkZBYBZmQYAgUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFtsBBRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDAFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkMQUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQyBRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDMFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkNAUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQ1BRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDYFGGN0bDAwJGNwaE1haW4kY2JsR3JvdXAkNwUYY3RsMDAkY3BoTWFpbiRjYmxHcm91cCQ4BRhjdGwwMCRjcGhNYWluJGNibEdyb3VwJDgFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkMAUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxBRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDIFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkMwUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQ0BRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDUFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkNgUbY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQ3BRtjdGwwMCRjcGhNYWluJGNibENhdGVnb3J5JDgFG2N0bDAwJGNwaE1haW4kY2JsQ2F0ZWdvcnkkOQUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMAUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMQUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMgUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxMwUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxNAUcY3RsMDAkY3BoTWFpbiRjYmxDYXRlZ29yeSQxNAUYY3RsMDAkY3BoTWFpbiRjYmxMZXZlbCQwBRhjdGwwMCRjcGhNYWluJGNibExldmVsJDEFGGN0bDAwJGNwaE1haW4kY2JsTGV2ZWwkMgUYY3RsMDAkY3BoTWFpbiRjYmxMZXZlbCQzBRhjdGwwMCRjcGhNYWluJGNibExldmVsJDMFHWN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZyQwBR1jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmckMQUdY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nJDIFHWN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZyQzBR1jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmckNAUdY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nJDUFHWN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZyQ1BR5jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmc1JDAFHmN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZzUkMQUeY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nNSQyBR5jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmc1JDMFHmN0bDAwJGNwaE1haW4kY2JsU3RhclJhdGluZzUkNAUeY3RsMDAkY3BoTWFpbiRjYmxTdGFyUmF0aW5nNSQ1BR5jdGwwMCRjcGhNYWluJGNibFN0YXJSYXRpbmc1JDUFImN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYll0ZDIFImN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYll0ZDEFImN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYll0ZDEFIWN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYk0zMgUhY3RsMDAkY3BoTWFpbiR1Y1BlcmZvcm1hbmNlJHJiTTMxBSFjdGwwMCRjcGhNYWluJHVjUGVyZm9ybWFuY2UkcmJNMzEFIWN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYk02MgUhY3RsMDAkY3BoTWFpbiR1Y1BlcmZvcm1hbmNlJHJiTTYxBSFjdGwwMCRjcGhNYWluJHVjUGVyZm9ybWFuY2UkcmJNNjEFIWN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYlkxMgUhY3RsMDAkY3BoTWFpbiR1Y1BlcmZvcm1hbmNlJHJiWTExBSFjdGwwMCRjcGhNYWluJHVjUGVyZm9ybWFuY2UkcmJZMTEFIWN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYlkyMgUhY3RsMDAkY3BoTWFpbiR1Y1BlcmZvcm1hbmNlJHJiWTIxBSFjdGwwMCRjcGhNYWluJHVjUGVyZm9ybWFuY2UkcmJZMjEFIWN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYlkzMgUhY3RsMDAkY3BoTWFpbiR1Y1BlcmZvcm1hbmNlJHJiWTMxBSFjdGwwMCRjcGhNYWluJHVjUGVyZm9ybWFuY2UkcmJZMzEFIWN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYlk1MgUhY3RsMDAkY3BoTWFpbiR1Y1BlcmZvcm1hbmNlJHJiWTUxBSFjdGwwMCRjcGhNYWluJHVjUGVyZm9ybWFuY2UkcmJZNTEFImN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYlkxMDIFImN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYlkxMDEFImN0bDAwJGNwaE1haW4kdWNQZXJmb3JtYW5jZSRyYlkxMDEFGmN0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQwBRpjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMQUaY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDIFGmN0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQzBRpjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNAUaY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDUFGmN0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ2BRpjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNwUaY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDgFGmN0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ5BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTAFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQxMQUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDEyBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTMFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQxNAUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDE1BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTYFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQxNwUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDE4BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTkFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQyMAUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDIxBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMjIFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQyMwUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDI0BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMjUFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQyNgUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDI3BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMjgFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQyOQUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDMwBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMzEFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQzMgUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDMzBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMzQFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQzNQUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDM2BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMzcFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQzOAUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDM5BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNDAFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ0MQUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDQyBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNDMFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ0NAUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDQ1BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNDYFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ0NwUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDQ4BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNDkFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ1MAUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDUxBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNTIFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ1MwUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDU0BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNTUFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ1NgUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDU3BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNTgFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ1OQUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDYwBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNjEFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ2MgUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDYzBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNjQFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ2NQUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDY2BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNjcFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ2OAUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDY5BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNzAFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ3MQUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDcyBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNzMFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ3NAUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDc1BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNzYFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ3NwUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDc4BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkNzkFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ4MAUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDgxBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkODIFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ4MwUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDg0BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkODUFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ4NgUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDg3BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkODgFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ4OQUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDkwBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkOTEFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ5MgUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDkzBRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkOTQFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ5NQUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDk2BRtjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkOTcFG2N0bDAwJGNwaE1haW4kY2JsQ29tcGFueSQ5OAUbY3RsMDAkY3BoTWFpbiRjYmxDb21wYW55JDk5BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTAwBRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTAxBRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTAyBRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTAzBRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTA0BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTA1BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTA2BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTA3BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTA4BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTA5BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTEwBRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTExBRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTEyBRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTEzBRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTE0BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTE1BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTE2BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTE3BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTE4BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTE5BRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTIwBRxjdGwwMCRjcGhNYWluJGNibENvbXBhbnkkMTIwBRxjdGwwMCRjcGhNYWluJGNibFBvcnRmb2xpbyQwBRxjdGwwMCRjcGhNYWluJGNibFdhdGNoTGlzdCQwBRxjdGwwMCRjcGhNYWluJGNibFdhdGNoTGlzdCQwBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMDIkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDAzJGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwwNCRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMDUkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDA2JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwwNyRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMDgkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDA5JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwxMCRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMTEkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDEyJGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwxMyRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMTQkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDE1JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwxNiRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMTckY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDE4JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwxOSRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMjAkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDIxJGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwyMiRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMjMkY2hrRnVuZAUmY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0JGN0bDI0JGNoa0Z1bmQFJmN0bDAwJGNwaE1haW4kZ3JpZFJlc3VsdCRjdGwyNSRjaGtGdW5kBSZjdGwwMCRjcGhNYWluJGdyaWRSZXN1bHQkY3RsMjYkY2hrRnVuZAUYY3RsMDAkY3BoTWFpbiRncmlkUmVzdWx0DzwrAAoBCAIBZNDz1q2PxpNYmuiI0RgvYPOPx2hZ",
        "ctl00$cphMain$hfStylebox":"0,0,0,0,0,0,0,0,0",
        "ctl00$cphMain$hfRisk":"0,0,0,0",
        "ctl00$cphMain$ucPerformance$YTD":"rbYtd2",
        "ctl00$cphMain$ucPerformance$txtYtd":"",
        "ctl00$cphMain$ucPerformance$Month3":"rbM32",
        "ctl00$cphMain$ucPerformance$txtM3":"",
        "ctl00$cphMain$ucPerformance$Month6":"rbM62",
        "ctl00$cphMain$ucPerformance$txtM6":"",
        "ctl00$cphMain$ucPerformance$Year1":"rbY12",
        "ctl00$cphMain$ucPerformance$txtY1":"",
        "ctl00$cphMain$ucPerformance$Year2":"rbY22",
        "ctl00$cphMain$ucPerformance$txtY2":"",
        "ctl00$cphMain$ucPerformance$Year3":"rbY32",
        "ctl00$cphMain$ucPerformance$txtY3":"",
        "ctl00$cphMain$ucPerformance$Year5":"rbY52",
        "ctl00$cphMain$ucPerformance$txtY5":"",
        "ctl00$cphMain$ucPerformance$Year10":"rbY102",
        "ctl00$cphMain$ucPerformance$txtY10":"",
        "ctl00$cphMain$ddlEffectiveDate":"G",
        "ctl00$cphMain$txtEffectiveDate":"",
        "ctl00$cphMain$ddlFundStatus":"",
        "ctl00$cphMain$hfTNA":"0~5",
        "ctl00$cphMain$hfMinInvest":"0~5",
        "ctl00$cphMain$txtFund":"",
        "ctl00$cphMain$hfMoreOptions":"close",
        "ctl00$cphMain$ddlPageSite":"10000"
    }

    responseHtml = requestData(reqUrl, data)
    soup = BeautifulSoup(responseHtml.text, "lxml")
    # print responseHtml.text
    print soup.prettify()

    summaryData = soup.find(id='ctl00_cphMain_TotalResultLabel')
    print "summaryData: ",summaryData
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
        code = tds[1].find("a").get_text()

        newMutualFundReturnInfo = MutualFundReturnInfo.objects.filter(code=code)
        if newMutualFundReturnInfo :
            newMutualFundReturnInfo = newMutualFundReturnInfo[0]
            print "get MutualFundReturnInfo saved info is: ", MutualFundReturnInfo
        else:
            print "get MutualFundReturnInfo saved info is null, create new one.code:",code
            newMutualFundReturnInfo = MutualFundReturnInfo(code=code)

        i = 2
        newMutualFundReturnInfo.name = tds[i].find("a").get_text()
        print "code:",code,"name:",newMutualFundReturnInfo.name
        i += 1
        newMutualFundReturnInfo.oneDayReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.oneWeekReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.oneMonthReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.threeMonthReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.sixMonthReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.oneYearReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.twoYearReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.threeYearReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.fiveYearReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.tenYearReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.totalReturn = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.threeYearStandard = convertStringToFloat(tds[i].get_text())
        i += 1
        newMutualFundReturnInfo.threeYearRisk = convertStringToFloat(tds[i].get_text())
        newMutualFundReturnInfo.updateDate = date
        print "newMutualFundReturnInfo is:",newMutualFundReturnInfo
        newMutualFundReturnInfo.save()
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