import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

industryCodeList=instCpCodeMgr.GetIndustryList() #업종별 코드 리스트
# for industryCode in industryCodeList:
#     print(industryCode, instCpCodeMgr.GetIndustryName(industryCode))



#업종 코드에 해당하는 종목 코드 리스트
targetCodeList=instCpCodeMgr.GetIndustryGroupCodeList('KGS01P')

for code in targetCodeList:
    print(code, instCpCodeMgr.CodeToName(code))

instMarketEye=win32com.client.Dispatch("CpSysDib.MarketEye")