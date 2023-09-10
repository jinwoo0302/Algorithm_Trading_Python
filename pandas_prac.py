from pandas import Series, DataFrame

kakao=Series([92600,92400,92100,94300,92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
print(kakao)
print(kakao['2016-02-19'])
print(kakao['2016-02-18'])
for date in kakao.index:
    print(date)

for ending_price in kakao.values:
    print(ending_price)

mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])
merge=mine+friend
print(merge)