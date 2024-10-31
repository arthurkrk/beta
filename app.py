import streamlit as st
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objs as go

import yfinance as yf
import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"

# Specify title and logo for the webpage.
# Set up your web app
st.set_page_config(layout="wide", page_title="WebApp_Demo")

# Sidebar
st.sidebar.title("Input Ticker")
symbol = st.sidebar.text_input('Please enter the stock symbol: ', 'NVDA').upper()
# Selection for a specific time frame.
col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    sdate = st.date_input('Start Date',value=datetime.date(2024,1,1))
with col2:
    edate = st.date_input('End Date',value=datetime.date.today())

st.title(f"{symbol}")

stock = yf.Ticker(symbol)
if stock is not None:
  # Display company's basics
  st.write(f"# Sector : {stock.info['sector']}")
  st.write(f"# Company Beta : {stock.info['beta']}")
  st.write(f"# Company Market Cap : {stock.info['marketCap']}")
  st.write(f"# Company Employees : {stock.info['fullTimeEmployees']}")
else:
  st.error("Failed to fetch historical data.")

data = yf.download(symbol,start=sdate,end=edate)
if data is not None:
  st.line_chart(data['Close'],x_label="Date",y_label="Close")
  st.write(data.describe)
else:
    st.error("Failed to fetch historical data.")
