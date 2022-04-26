import streamlit as st
import pandas as pd
import numpy as np
import pandas_datareader as web
import mplfinance as mpf
import datetime as dt


st.title("Stock Price Analysis")

#Multiselect box to get the charts and info of the stocks
tickerSymbol = st.multiselect('Select the ticker symbols of the stocks',('TSLA','TWTR','GOOGL','AMZN','FB','AAPL', 'NFLX'))

#get the closing price of the stocks using mplfinance
def get_close_stock_price_mplfinance(symbols, start_date, end_date):
    df = pd.DataFrame()
    for symbol in symbols:
        df[symbol] = web.DataReader(symbol, 'yahoo', start_date, end_date)['Adj Close']
    return df


#get the volume of the stocks using mplfinance
def get_volume_stock_price_mplfinance(symbols, start_date, end_date):
    df = pd.DataFrame()
    for symbol in symbols:
        df[symbol] = web.DataReader(symbol, 'yahoo', start_date, end_date)['Volume']
        df[symbol] = df[symbol].astype(int)
    return df

#get the closing price of the stocks end date to be today
start_date = st.sidebar.date_input('Start Date', value=pd.Timestamp('2021-04-01'))
end_date = st.sidebar.date_input('End Date', value=pd.Timestamp('2022-04-26'))

#based on dates selected and stocks selected get the line charts for the shares
df = get_close_stock_price_mplfinance(tickerSymbol, start_date, end_date)

#get the volume of the stocks end date to be today
df_volume = get_volume_stock_price_mplfinance(tickerSymbol, start_date, end_date)

#line chart for the closing price of the stocks
st.header('Stock Closing Price' + ' (' + start_date.strftime('%Y-%m-%d') + ' to ' + end_date.strftime('%Y-%m-%d') + ')')
st.line_chart(df, width=800, height=400, use_container_width=True)

#line chart for the volume of the stocks
st.header('Stock Volume' + ' (' + start_date.strftime('%Y-%m-%d') + ' to ' + end_date.strftime('%Y-%m-%d') + ')')
st.bar_chart(df_volume, width=800, height=400, use_container_width=True)

#create a container and inside that put two columns and in two columns put the line chart and the volume chart
st.header('Analysis of the Stocks')

#select window size
window_size = st.slider('Select the window size', 10, 30, 5)

#get the moving average of the stocks
def get_moving_average(df, window):
    ma = df.rolling(window=window).mean()
    return ma

#get the moving average of the stocks
def get_moving_average_volume(df_volume, window):
    ma = df_volume.rolling(window=window).mean()
    return ma

#get the moving average of the stocks
def get_momentum(df, window):
    momentum = df.diff(window)
    return momentum

#get the moving average of the stocks
def get_momentum_volume(df, window):
    momentum = df.diff(window)
    return momentum

col1, col2  = st.columns(2)

col1.subheader('Moving Average')
col1.bar_chart(get_moving_average(df, window_size))

col2.subheader('Moving Average Volume')
col2.bar_chart(get_moving_average_volume(df_volume, window_size))

col3, col4 = st.columns(2)

col3.subheader('Momentum')
col3.bar_chart(get_momentum(df, window_size))

col4.subheader('Momentum Volume')
col4.bar_chart(get_momentum_volume(df_volume, window_size))

