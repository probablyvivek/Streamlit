#get share price of Tesla and Twitter of last 6 months and create a streamlit app

import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title("Stock Price Analysis")

#Multiselect box to get the charts and info of the stocks
tickerSymbol = st.multiselect('Select the ticker symbols of the stocks',('TSLA','TWTR','GOOGL','AMZN','FB','AAPL'))

#get the closing price of the stocks
def get_close_stock_price(symbols, start_date, end_date):
    df = pd.DataFrame()
    for symbol in symbols:
        df[symbol] = yf.download(symbol, start_date, end_date)['Adj Close']
    return df

#get the volume of the stocks
def get_volume_stock_price(symbols, start_date, end_date):
    df = pd.DataFrame()
    for symbol in symbols:
        df[symbol] = yf.download(symbol, start_date, end_date)['Volume']
        df[symbol] = df[symbol].astype(int)
    return df

#get the closing price of the stocks end date to be today
start_date = st.sidebar.date_input('Start Date', value=pd.Timestamp('2020-01-01'))
end_date = st.sidebar.date_input('End Date', value=pd.Timestamp('2020-06-01'))

#based on dates selected and stocks selected get the line charts for the shares
df = get_close_stock_price(tickerSymbol, start_date, end_date)

#get the volume of the stocks
df_volume = get_volume_stock_price(tickerSymbol, start_date, end_date)

#line chart for the closing price of the stocks
st.header('Stock Closing Price' + ' (' + start_date.strftime('%Y-%m-%d') + ' to ' + end_date.strftime('%Y-%m-%d') + ')')
st.area_chart(df, width=800, height=400, use_container_width=True)

#line chart for the volume of the stocks
st.header('Stock Volume' + ' (' + start_date.strftime('%Y-%m-%d') + ' to ' + end_date.strftime('%Y-%m-%d') + ')')
st.bar_chart(df_volume, width=800, height=400, use_container_width=True)


