import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd  # Import pandas for date handling

# Set the title of the Streamlit app
st.title("Stock Price Dashboard")

# Sidebar inputs for user
st.sidebar.header("Select Stock and Date Range")
ticker_symbol = st.sidebar.text_input("Stock Ticker Symbol", "AAPL")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))

# Fetch stock data
def get_stock_data(symbol, start, end):
    stock_data = yf.download(symbol, start=start, end=end)
    return stock_data

# Fetch and display stock data when button is clicked
if st.sidebar.button("Show Stock Data"):
    stock_data = get_stock_data(ticker_symbol, start_date, end_date)
    
    # Display stock data as a line chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title=f"{ticker_symbol} Stock Price", xaxis_title="Date", yaxis_title="Close Price (USD)")
    st.plotly_chart(fig)
    
    # Show summary statistics
    st.write("## Stock Data Summary")
    st.write(stock_data.describe())
    
    # Show raw data
    st.write("## Raw Data")
    st.write(stock_data)

# Note on usage
st.sidebar.info("Enter a stock ticker symbol (e.g., AAPL for Apple, TSLA for Tesla), select a date range, and click 'Show Stock Data' to visualize the stock prices.")
