import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf



class Chart():
    def __init__(self): 
        self.fig = make_subplots(
            rows=2, cols=1,  # 2 rows, 1 column
            shared_xaxes=True,  # Share x-axis between plots
            vertical_spacing=0.02,  # Spacing between the two plots
            row_heights=[0.7, 0.3]  # Height ratios for the plots
        ) 

    def candlechart(self, df, ticker):

        # df_reset = df.reset_index() 
        self.fig = go.Figure(data=[go.Candlestick(
            x=df['Date'], 
            open=df['Open'][ticker],
            high=df['High'][ticker],
            low=df['Low'][ticker],
            close=df['Close'][ticker], 
            name='Candlestick'
        )]) 

        # Update layout
        self.fig.update_layout(
            title="Stock Data: AAPL",
            xaxis_title="Date",
            yaxis_title="Price (USD)",
            xaxis_rangeslider_visible=False, 
            dragmode='pan',  # Enable panning mode
            template="plotly_dark"  # Optional dark theme 
        ) 


        # self.moving_averages(df) 

        config = {'scrollZoom': True}  

        # Show plot
        self.fig.show(config=config) 

    
    def moving_averages(self, df, stock_symbol): 
        # Calculate moving averages 

        df['SMA_50'] = df['Close'][stock_symbol].rolling(window=50).mean()
        df['SMA_200'] = df['Close'][stock_symbol].rolling(window=200).mean()

        # Adding moving averages to the candlestick chart
        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                            open=df['Open'][stock_symbol],
                                            high=df['High'][stock_symbol],
                                            low=df['Low'][stock_symbol],
                                            close=df['Close'][stock_symbol],
                                            name='Candlestick'),
                            go.Scatter(x=df['Date'], y=df['SMA_50'], line={'color': 'orange'}, name='50-Day SMA'),
                            go.Scatter(x=df['Date'], y=df['SMA_200'], line={'color': 'blue'}, name='200-Day SMA')])

        fig.update_layout(title="Stock Data with Moving Averages: AAPL",
                        xaxis_title="Date",
                        yaxis_title="Price (USD)",
                        xaxis_rangeslider_visible=False)
 
        fig.show() 
