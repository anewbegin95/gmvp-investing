import yfinance as yf
import pandas as pd

ticker = 'AAPL'
portfolio_data = pd.DataFrame()

ticker_obj = yf.Ticker(ticker)
data = ticker_obj.history(start='2023-01-01', end='2023-03-30', interval="1d")
data['Ticker'] = ticker
portfolio_data = pd.concat([portfolio_data, data])
print(portfolio_data)