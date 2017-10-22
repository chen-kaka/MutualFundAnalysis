
from Service import fetchBankGoldData,fetchFundData,fetchNetData
import time

def testScheduler():
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print date + ": hello scheduler!"

def fetchBankGoldDataScheduler():
    fetchBankGoldData.fetchBankGoldDataReq()

def fetchFundDataScheduler():
    fetchFundData.fetchMutualFundData()

def fetchNetDataScheduler():
    fetchNetData.fetchNetDataReq()