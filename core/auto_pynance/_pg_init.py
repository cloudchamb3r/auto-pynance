from auto_pynance.dump.usdm import dump_usdm
from datetime import datetime, timedelta
from peewee import *
from dotenv import load_dotenv
import os

load_dotenv()
db = PostgresqlDatabase(
    database    = os.getenv("POSTGRES_DB"),
    host        = os.getenv("POSTGRES_HOST"),
    port        = os.getenv("POSTGRES_PORT"), 
    user        = os.getenv("POSTGRES_USER"),
    password    = os.getenv("POSTGRES_PASS")
)

# base model def
class BaseModel(Model):
    class Meta:
        database = db

# ticker_data def 
class TickerData(BaseModel):
    # pk
    market                  = CharField()
    symbol                  = CharField()
    interval                = CharField()
    open_time               = BigIntegerField()

    # non-pk
    open                    = FloatField()
    high                    = FloatField()
    low                     = FloatField()
    close                   = FloatField()
    volume                  = FloatField()
    close_time              = BigIntegerField()
    count                   = IntegerField()
    quote_volume            = FloatField()
    taker_buy_volume        = FloatField()
    taker_buy_quote_volume  = FloatField()

    class Meta:
        table_name  = "ticker_data"
        primary_key = CompositeKey('market', 'symbol', 'interval', 'open_time')

def pg_init():
    db.create_tables([TickerData])

    start_date = datetime(2020, 1, 1)
    end_date = datetime.today()

    current_date = start_date
    while current_date <= end_date:
        try:
            dump = dump_usdm('BTCUSDT', current_date)
            current_date += timedelta(days = 1)
            if dump == None: continue
            for elem in dump:
                open_time, open, high, low, close, volume, close_time, count, \
                quote_volume, taker_buy_volume, taker_buy_quote_volume = elem
                TickerData.insert(
                    market = "USDM", 
                    symbol = "BTCUSDT",
                    interval = "1m",
                    open_time = open_time,
                    open = open,
                    high = high,   
                    low = low,
                    close = close,
                    volume = volume,
                    close_time = close_time,
                    count = count, 
                    quote_volume = quote_volume,
                    taker_buy_volume = taker_buy_volume,
                    taker_buy_quote_volume = taker_buy_quote_volume,
                ).execute()
        except Exception as e:
            print(f"[!] err : {e}")
             
if __name__ == '__main__':
    pg_init()