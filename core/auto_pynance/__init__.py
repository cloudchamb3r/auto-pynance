from enum import Enum
import requests
from datetime import datetime
from typing import Optional
import zipfile
import io 
import auto_pynance

# global session for dump
sess = requests.session()

class MarketType(Enum):
    USDM = "USDM"
    COINM = "COINM"

class OrderType(Enum):
    BUY = "BUY"
    SELL = "SELL"

class MarginType(Enum):
    ISOLATED = "ISOLATED"
    CROSSED = "CROSSED"

def dump(market_type : MarketType, symbol: str, date : datetime, interval = '1m') -> Optional[list[tuple[
        int,        # open_time
        float,      # open
        float,      # high
        float,      # low
        float,      # close
        float,      # volume
        int,        # close_time
        float,      # quote volume
        int,        # count
        float,      # taker_buy_volume
        float,      # taker_buy_quote_volume
    ]]]:
    try:
        mt = 'um' if market_type == auto_pynance.MarketType.USDM else 'cm'
        target = f'{symbol}-{interval}-{date.year:04}-{date.month:02}-{date.day:02}'
        target_url = f'https://data.binance.vision/data/futures/{mt}/daily/klines/{symbol}/{interval}/{target}.zip'
        res = sess.get(target_url)
        if res.content[0:2] == b'PK':
            file = io.BytesIO(res.content)
            with zipfile.ZipFile(file, 'r') as z:
                data = z.read(f'{target}.csv').split()
                ret = []
                for line in data:
                    if line.startswith(b'o'): continue
                    open_time, open, high, low, close, volume, \
                    close_time, quote_volume,count,taker_buy_volume\
                    ,taker_buy_quote_volume, *_ =  line.decode(encoding='utf-8').split(",")
                    ret.append((
                        int(open_time), 
                        float(open), 
                        float(high), 
                        float(low), 
                        float(close), 
                        float(volume),
                        int(close_time), 
                        float(quote_volume), 
                        int(count),
                        float(taker_buy_volume), 
                        float(taker_buy_quote_volume),
                    ))
                return ret
    except Exception as e:
        print(f"[!]dump error : {e}")
    return None
