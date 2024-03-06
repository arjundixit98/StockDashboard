import streamlit as st, yfinance as yf
import plotly.express as px

st.title('Stock Dashboard')

ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start date')
end_date = st.sidebar.date_input('End Date')


data = yf.download(ticker,start=start_date, end=end_date)
fig = px.line(data, x=data.index, y = data['Adj Close'], title = ticker)
st.plotly_chart(fig)

print('Hello World')