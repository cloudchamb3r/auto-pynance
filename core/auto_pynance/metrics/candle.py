import numpy as np
from typing import Self

class Candle:
    # price/volume information
    open_price  : np.array[float]
    high_price  : np.array[float]
    low_price   : np.array[float]
    close_price : np.array[float]
    volume      : np.array[float]

    # epoch time 
    open_time   : np.array[int]
    duration    : np.array[int]

    def __init__(
            self, 
            open_price  : np.array[float], 
            high_price  : np.array[float], 
            low_price   : np.array[float], 
            close_price : np.array[float], 
            volume      : np.array[float], 
            open_time   : np.array[int], 
            duration    : np.array[int]
    ) -> None:
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.volume = volume
        self.open_time = open_time
        self.duration = duration

    def try_parse_binance_line(line : str) -> Self:
        open_time, open_price, high_price ,low_price, close_price, volume, close_time, *_ = line.split(',')

        open_price = float(open_price)
        high_price = float(high_price)
        low_price = float(low_price)
        close_price = float(close_price)
        volume = float(volume)

        open_time = int(open_time)
        duration = int(close_time) - open_time
        
        return Candle(
            open_price  = open_price, 
            high_price  = high_price, 
            low_price   = low_price, 
            close_price = close_price, 
            volume      = volume, 
            open_time   = open_time, 
            duration    = duration,
        )