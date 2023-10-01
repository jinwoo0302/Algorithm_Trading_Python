import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import datetime
import mplfinance as mpf
from matplotlib import font_manager, rc, style



# plt.plot([1,2,3.5,4])
# plt.show()

# x=range(0,100)
# y=[v*v for v in x]
# plt.plot(x,y,'g^')
# plt.show()

# x=np.arange(0.0, 2*np.pi,0.1)
# sin_y=np.sin(x)
# cos_y=np.cos(x)
#
# fig=plt.figure()
# ax1=fig.add_subplot(211)
# ax2=fig.add_subplot(212)
#
# ax1.plot(x,sin_y,'b--')
# ax2.plot(x,cos_y,'r--')
#
# ax1.set_xlabel('x')
# ax1.set_ylabel('sin(x)')
#
# ax2.set_xlabel('x')
# ax2.set_ylabel('cos(x')




# lg=yf.download("066570.KS")
# samsung=yf.download("005930.KS")
#
# plt.plot(lg.index, lg['Adj Close'], label='LG Electronics')
# plt.plot(samsung.index, samsung['Adj Close'], label="samsung Electronics")
#
# plt.legend(loc='best')


# fig=plt.figure()
# ax=fig.add_subplot(111)
# type(ax)
# plt.show()

# fig, ax_list = plt.subplots(2,2)
#
# ax_list[0][0].plot([1,2,3,4])


# sk_hynix=yf.download("000660.KS")

# fig=plt.figure(figsize=(12,8))
#
# top_axes=plt.subplot2grid((4,4),(0,0),rowspan=3, colspan=4)
# bottom_axes=plt.subplot2grid((4,4),(3,0),rowspan=1, colspan=4)
# bottom_axes.get_yaxis().get_major_formatter().set_scientific(False) #오일러 상수의 지수 형태 금지
#
# top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], label='Adjusted Close')
# bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'])
#
# plt.tight_layout




# start=datetime.datetime(2016,3,1)
# end=datetime.datetime(2016,3,31)
# sk_hynix=yf.download("000660.KS",start,end)
#
# day_list=[]
# name_list=[]
# for i , day in enumerate(sk_hynix.index):
#     if day.dayofweek==0:
#         day_list.append(i)
#         name_list.append(day.strftime('%Y-%m-%d')+'(Mon)')
#
# mpf.plot(sk_hynix, type="candle",style=make_mpf_style,figsize=(12,8))



# 봉차트(가로, 세로)
# font_name=font_manager.FontProperties(fname="c:/windows/Fonts/malgun.ttf").get_name()
# rc('font',family=font_name)
# style.use('ggplot')
#
# industry = ['통신업', '의료정밀', '운수창고업', '의약품', '음식료품', '전기가스업', '서비스업', '전기전자', '종이목재', '증권']
# fluctuations = [1.83, 1.30, 1.30, 1.26, 1.06, 0.93, 0.77, 0.68, 0.65, 0.61]
#
# fig=plt.figure(figsize=(12,8))
# ax=fig.add_subplot(111)
#
# pos=np.arange(10)
# rects=plt.bar(pos,fluctuations,align='center', width=0.5)
# plt.xticks(pos,industry)
#
# for i, rect in enumerate(rects):
#     ax.text(rect.get_x() +rect.get_width()/2.0, 0.9*rect.get_height(),
#             str(fluctuations[i]) + '%', ha='center')


# plt.ylabel('등락률')




#파이차트
font_name=font_manager.FontProperties(fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
style.use('ggplot')

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
labels = ['삼성전자', 'SK하이닉스', 'LG전자', '네이버', '카카오']
ratio = [50, 20, 10, 10, 10]
explode=(0.0, 0.2, 0.0, 0.0, 0.0)

plt.pie(ratio,explode=explode,labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=120)

plt.show()