import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
import pandas as pd
import pandas_datareader as web 
import seaborn

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

symbols_list = ['IDN', 'APT', 'WTRH', 'SLV' , 'SUMR', 'SMSI']
start = datetime(2020, 1, 1)

symbols =[]

for ticker in symbols_list: 
    r = web.DataReader(ticker, 'yahoo', start)
    r['Symbol'] = ticker
    symbols.append(r)

df = pd.concat(symbols)
df = df.reset_index()
df = df[['Date', 'Close', 'Symbol']]
df.head()
df_pivot = df.pivot('Date','Symbol','Close').reset_index()
df_pivot.head()

corr_df = df_pivot.corr(method='pearson')
#reset symbol as index (rather than 0-X)
corr_df.head().reset_index()
corr_df.head(10)
rounding = np.round(corr_df, 2)
print(rounding)

mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True
#generate plot
seaborn.heatmap(corr_df, cmap='RdYlGn', vmax=1.0, vmin=-1.0 , mask = mask, linewidths=2.5)
plt.yticks(rotation=0) 
plt.xticks(rotation=90) 
plt.show()