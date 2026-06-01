import yfinance as yf
import plotly.graph_objects as go
import time

ticker = "TSLA"

df = yf.download(tickers=ticker, period="6mo", interval="1d", rounding=True) 
print(type(df)) 

print(df.columns)
df.columns=["Close", "High", "Low", "Open", "Volume"] 
print(df.head())
df=df.reset_index() 
print(df.head())

chart = go.Figure()
chart.add_trace(go.Candlestick(
    x=df["Date"],
    open=df["Open"],
    high=df["High"],
    low=df["Low"],
    close=df["Close"],
    name="Price chart"
    ))
chart.update_layout(title=f"Ticker - {ticker} share price", yaxis_title="Stock Price(USD)")
chart.show()
