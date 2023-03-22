from typing import List
from auto_pynance.metrics.candle import Candle


def gen_heikinashi(candles: List[Candle]) -> List[Candle]:
    ret = []
    for i, candle in enumerate(candles):
        ref_candle = candles[i - 1] if i != 0 else candles[i]    

        # calculate open price, close price
        open_price = (ref_candle.open_price + ref_candle.close_price) / 2
        close_price = (candle.open_price + candle.close_price + candle.low_price + candle.high_price) / 4
        candle.open_price = open_price
        candle.close_price = close_price

        # caculate high price, low price
        high_price = max(candle.high_price, candle.open_price, candle.close_price)
        low_price = min(candle.low_price, candle.open_price, candle.close_price)
        candle.high_price = high_price
        candle.low_price = low_price

        ret.append(candle)
    return ret
