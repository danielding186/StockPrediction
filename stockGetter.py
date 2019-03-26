from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
from functools import reduce

tickers = []

tickers.append('AMZN')

# indexs
tickers.extend(['^DJI', '^GSPC', '^NDX'])

# Treasury Yield
tickers.extend(['^IRX', '^FVX', '^TNX', '^TYX'])

# other countries index
tickers.extend(['000001.SS', '^HSI', '^N225', '^FCHI', '^GDAXI',  '^BSESN'])

# other companies
tickers.extend(['AAPL', 'FB', 'GOOG', 'NFLX', 'EBAY', 'CRM', 'MSFT', 'WMT'])

start_date = '2014-1-1'
end_date = '2018-12-31'

frames = []
for ticker in tickers:
    stock_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
    stock_data = stock_data.rename(lambda s: (s.lower() + '-' + ticker).replace(' ', '-'), axis='columns')
    frames.append(stock_data)

df_final = reduce(lambda left,right: left.join(right), frames)

df_final.to_excel("output.xlsx")