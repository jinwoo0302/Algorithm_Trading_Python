import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

industryCodeList=instCpCodeMgr.GetIndustryList() #업종별 코드 리스트
# for industryCode in industryCodeList:
#     print(industryCode, instCpCodeMgr.GetIndustryName(industryCode))



#업종 코드에 해당하는 종목 코드 리스트
targetCodeList=instCpCodeMgr.GetIndustryGroupCodeList('KGS01P')

for code in targetCodeList:
    print(code, instCpCodeMgr.CodeToName(code))

#각 종목의 PER 값은 CpSyDib 모듈의 MarketEye 클래스를 사용해 얻을 수 있었습니다.
instMarketEye=win32com.client.Dispatch("CpSysDib.MarketEye")

instMarketEye.SetInputValue(0, 67)
instMarketEye.SetInputValue(1,targetCodeList) #코드 리스트 던져주기

instMarketEye.BlockRequest() #요청 보내기

numStock=instMarketEye.GetHeaderValue(2)#값 개수 받아오기.

sumPer=0
for i in range(numStock):
    sumPer+=instMarketEye.GetDataValue(0,i)

print("Average Per: ",sumPer/numStock)

