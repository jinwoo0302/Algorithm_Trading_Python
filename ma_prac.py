import pandas as pd
import yfinance as yf

gs=yf.download("078930.KS", "2014-01-01", "2016-03-06")

#print(gs)

print(gs.tail())

ma5=gs['Adj Close'].rolling(window=5).mean()

print(type(ma5))
print(ma5.tail(10))