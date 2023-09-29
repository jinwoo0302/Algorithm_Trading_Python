import yfinance as yf
import datetime
import pandas as pd
import matplotlib.pyplot as plt



print(yf.__version__)
print(pd.__version__)

start_date = datetime.datetime(2021, 1, 1)
end_date = datetime.datetime(2021, 12, 31)

df = yf.download('078930.KS')

plt.plot(df.index, df['Adj Close'])
plt.show()