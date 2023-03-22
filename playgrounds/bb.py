# this source shows simple example of using ta-lib

import numpy as np 
import pandas as pd 
import auto_pynance.ta as ta
import matplotlib.pyplot as plt

stock_data = pd.read_csv("./usdm-data/BTCUSDT-1m-2021-01-01.csv")


upper, middle, lower = ta.bbands(stock_data["close"], timeperiod = 14)

# draw plot
plt.plot(stock_data["close"])
plt.plot(upper)
plt.plot(middle)
plt.plot(lower)
plt.show()