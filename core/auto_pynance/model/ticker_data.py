from auto_pynance.model import BaseModel
from peewee import * 

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
    quote_volume            = FloatField()
    count                   = IntegerField()
    taker_buy_volume        = FloatField()
    taker_buy_quote_volume  = FloatField()

    class Meta:
        table_name  = "ticker_data"
        primary_key = CompositeKey('market', 'symbol', 'interval', 'open_time')
