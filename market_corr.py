import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
import pandas as pd

stock1 = input('enter first ticker: ')
date1 = input('enter start date [YYYY-MM-DD]: ')
stock2 = input('enter second ticker: ')

Tick = yf.download(stock1, date1 , datetime.now().date())        #stock 1 dataframe
# print(Tick) #print dataframe1

Tickr = yf.download(stock2, date1 , datetime.now().date())        #stock 2 dataframe
# print(Tickr) #print dataframe2 

covariance = np.corrcoef(Tick['Close'], Tickr['Close'])
print(covariance)





