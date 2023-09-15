import time

import win32com.client
def CheckVolume(instStockChart,code):
    instStockChart.SetInputValue(0,code)
    instStockChart.SetInputValue(1,ord('2'))
    instStockChart.SetInputValue(4,60)#날짜 개수
    instStockChart.SetInputValue(5,8)#거래량
    instStockChart.SetInputValue(6, ord('D'))#일별
    instStockChart.SetInputValue(9,ord('1'))

    instStockChart.BlockRequest()

    volumes=[]
    numData=instStockChart.GetHeaderValue(3)
    for i in range(numData):
        volume=instStockChart.GetDataValue(0,i)
        volumes.append(volume)

    #평균 거래량 계산
    avaerageVolume=(sum(volumes)-volumes[0])/(len(volumes)-1)

    if(volumes[0]>avaerageVolume *10):
        return 1
    else:
        return 0

if __name__=="__main__":
    instCpCodeMgr=win32com.client.Dispatch("CpUtil.CpCodeMgr")
    codelist=instCpCodeMgr.GetStockListByMarket(1)

    instStockChart=win32com.client.Dispatch("CpSysDib.StockChart")
    buylist=[]
    for code in codelist:
        if CheckVolume(instStockChart,code)==1:
            buylist.append(code)
            print(code)
        time.sleep(0.01)