
from Service import fetchBankGoldData,fetchFundData,fetchNetData

def testScheduler():
    print "hello scheduler!"

def fetchBankGoldDataScheduler():
    fetchBankGoldData.fetchBankGoldDataReq()

def fetchFundDataScheduler():
    fetchFundData.fetchMutualFundData()

def fetchNetDataScheduler():
    fetchNetData.fetchNetDataReq()