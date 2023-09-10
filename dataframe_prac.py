from pandas import Series, DataFrame

raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data=DataFrame(raw_data)
print(data)



daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin)

print(daeshin_day)


daeshin_day=DataFrame(daeshin, columns=['open','high','low','close'])

print(daeshin_day)


date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)

print(daeshin_day)


close=daeshin_day['close']
print(close)

#print(daeshin_day['16.02.24'])
#pandas에서 []안에 들어가는 건 키 값으로 판단. 즉 열로 판단.
#행을 가져오고 싶다면 인덱스 값을 loc을 이용해서 넣어줘야 함.

day_data=daeshin_day.loc['16.02.24']
print(day_data)
print(type(day_data))

#인덱스와 칼럼 이름 확인법
print(daeshin_day.columns)
print(daeshin_day.index)


