import plotly.graph_objects as go
import pandas as pd
import yfinance as yf

# Fetch data
stock_symbol = "AAPL"
data = yf.download(stock_symbol, period="1y", interval="1d")


import pandas as pd

# Assuming 'data' is your DataFrame with the MultiIndex

# Reset the index to move 'Price' and 'Ticker' into columns
data_reset = data.reset_index() 

# Rename the columns if you want
data_reset.rename(columns={'Price': 'Date', 'Ticker': 'Stock'}, inplace=True)

# Now, the 'Date' will be a regular column
print(data_reset.head()) 


print(type(data_reset['Date']))
print(type(data_reset['Open']))

print(data_reset['Open'].columns)  

open_series = data_reset['Open'].squeeze()  
high_series = data_reset['High'].squeeze()  
low_series = data_reset['Low'].squeeze()  
close_series = data_reset['Close'].squeeze()  


# Create Candlestick Chart
fig = go.Figure(data=[go.Candlestick(
    x=data_reset['Date'],
    open=open_series,
    high=high_series,
    low=low_series,
    close=close_series,
    name='Candlestick'
)])

# Update layout
fig.update_layout(
    title="Stock Data: AAPL",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    xaxis_rangeslider_visible=False, 
    dragmode='pan',  # Enable panning mode
    template="plotly_dark"  # Optional dark theme 
) 


config = {'scrollZoom': True}  

# Show plot
fig.show(config=config) 


