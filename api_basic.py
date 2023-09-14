import win32com.client
instStockChart=win32com.client.Dispatch("CpSysDib.StockChart")

instStockChart.SetInputValue(0,"A003540")
instStockChart.SetInputValue(1,ord('1'))
instStockChart.SetInputValue(2,20230901)
instStockChart.SetInputValue(3,20230501)
#instStockChart.SetInputValue(4,10)
instStockChart.SetInputValue(5,(0,2,3,4,5,8))
instStockChart.SetInputValue(6,ord('D'))
instStockChart.SetInputValue(9,ord('1'))

instStockChart.BlockRequest()
numData=instStockChart.GetHeaderValue(3)
numField=instStockChart.GetHeaderValue(1)

field=(0,2,3,4,5,8)
field_list=['날짜','시간','시가','고가', '저가','종가', '전일대비', '거래량', '거래대금', '누적체결매도수량']
for i in range(numData):
    print()
    for j in range(numField):
        print(field_list[field[j]],": ",instStockChart.GetDataValue(j,i), end=" ") #첫 번째 인자는 데이터 인덱스(시가, 고가, 저가, 종가, 거래량 순서대로 0부터)
    print("")