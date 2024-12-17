import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch stock data
stock = 'AAPL'
data = yf.download(stock, start='2023-01-01', end='2023-12-31') 

print(type(data)) 
print(data.dtypes) 

data['RSI'] = 100 - (100 / (1 + data['Close'].pct_change().rolling(14).mean() / data['Close'].pct_change().rolling(14).std()))
data['SMA'] = data['Close'].rolling(20).mean()
data['Upper Band'] = data['SMA'] + 2 * data['Close'].rolling(20).std()
data['Lower Band'] = data['SMA'] - 2 * data['Close'].rolling(20).std()

# Plot
plt.figure(figsize=(14, 8))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['Upper Band'], label='Upper Band (Resistance)', color='red', linestyle='--')
plt.plot(data['Lower Band'], label='Lower Band (Support)', color='green', linestyle='--')
plt.title(f"{stock} Support/Resistance Analysis")
plt.legend()
plt.show()


