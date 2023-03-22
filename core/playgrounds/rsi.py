# this source shows simple example of using ta-lib

import numpy as np 
import pandas as pd 
import talib as ta
import matplotlib.pyplot as plt

stock_data = pd.read_csv("./usdm-data/BTCUSDT-1m-2021-01-01.csv")

fast_k = 14
slow_k = 3

rsi = ta.RSI(stock_data["close"], timeperiod = 14)
rsi_sma = ta.SMA(rsi, timeperiod = 14)

# draw plot
fig, (close_graph, rsi_graph) = plt.subplots(2, 1)
fig.suptitle("btc price with 14 rsi")

close_graph.set_label("btc price")
close_graph.plot(stock_data["close"])

rsi_graph.set_label("rsi graph with ma")
rsi_graph.plot(rsi)
rsi_graph.plot(rsi_sma)
plt.show()