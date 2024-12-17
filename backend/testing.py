import plotly.graph_objects as go
import yfinance as yf

# Fetch data
ticker = "AAPL"
data = yf.download(ticker, period="1y", interval="1d") 
data = data.reset_index()  


fig = go.Figure(data=[go.Candlestick(
    x=data['Date'], 
    open=data['Open'][ticker],
    high=data['High'][ticker],
    low=data['Low'][ticker],
    close=data['Close'][ticker], 
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


# moving_averages(df) 

config = {'scrollZoom': True}  

# Show plot
fig.show(config=config) 
