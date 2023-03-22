from datetime import datetime, timezone
from time import time

def current_binance_time(interval : int = 1):
    return 1000 * 60 * interval * (datetime.utcnow().timestamp() // (60 * interval))