"""
    HEIKINASHI + CE 
"""
import talib as ta

long_time_frame     = 33 
short_time_frame    = 5 
atr_period          = 13 
atr_multiplyer      = 2.8


long_heikin_atr = atr_multiplyer 
print(ta.ATR)
