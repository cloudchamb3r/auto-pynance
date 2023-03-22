# this source shows simple example of using ta-lib

import numpy as np 
import pandas as pd 
import talib as ta
import matplotlib.pyplot as plt

stock_data = pd.read_csv("./usdm-data/BTCUSDT-1m-2021-01-01.csv")

fast_k = 14
slow_k = 3

stochastic_fast, stochastic_slow = ta.STOCH(
                        stock_data["high"], 
                        stock_data["low"], 
                        stock_data["close"], 
                        fastk_period = fast_k,
                        slowk_period = slow_k, 
                        slowk_matype = 0, 
                        slowd_period=3, 
                        slowd_matype=0
                    )

fig, (close_graph, stochastic_graph) = plt.subplots(2, 1)
fig.suptitle("btc price with 14/3 stochastic")

close_graph.set_label("btc price")
close_graph.plot(stock_data["close"])

stochastic_graph.set_label("stochastic graph")
stochastic_graph.plot(stochastic_fast)
stochastic_graph.plot(stochastic_slow)
plt.show()