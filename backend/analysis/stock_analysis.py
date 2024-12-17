import yfinance as yf
import plotly.graph_objects as go
import pandas as pd 
import sys
import os
# Dynamically add the root directory to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) 
print(f"\033[92m Root Dir : {root_dir} \033[0m") 
sys.path.append(root_dir) 

from ploting.candle_stick import Chart 



def analysis(stock_symbol): 
    data = yf.download(stock_symbol, period="1y", interval="1d") 
    
    Chart().moving_averages(data, stock_symbol) 
    





