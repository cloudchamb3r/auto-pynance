# this source shows simple example of using ta-lib

import numpy as np 
import pandas as pd 
import talib as ta
import matplotlib.pyplot as plt

stock_data = pd.read_csv("./usdm-data/BTCUSDT-1m-2021-01-01.csv")

sma = ta.SMA(stock_data["close"], timeperiod=20)

plt.figure(figsize=(15, 5))
plt.plot(stock_data["close"])
plt.plot(sma, label="20min SMA")
plt.legend()
plt.show()