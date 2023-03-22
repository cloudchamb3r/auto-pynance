from binance.cm_futures import CMFutures
from binance.um_futures import UMFutures
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
from binance.websocket.cm_futures.websocket_client import CMFuturesWebsocketClient

from typing import Self, Union, Optional
from enum import Enum

from dotenv import load_dotenv



import os
import json
import sqlite3


def load_key_from_env() -> tuple[str, str]: 
    load_dotenv()
    api_key = os.getenv('API_KEY')
    secret_key = os.getenv('SECRET_KEY')

    if api_key == None or len(api_key) == 0: raise Exception("API_KEY is not specified in .env")
    if secret_key == None or len(secret_key) == 0: raise Exception("SECRET_KEY is not specified in .env")
    return (api_key, secret_key)

class FutureClientType(Enum):
    USD_M = 0
    COIN_M = 1

class FutureOrderType(Enum):
    LONG = "BUY"
    SHORT = "SELL"

class FutureMarginType(Enum):
    ISOLATED = "ISOLATED"
    CROSSED = "CROSSED"

class FutureClient():
    api_key     : str
    secret_key  : str

    ws_client   : Union[CMFuturesWebsocketClient, UMFuturesWebsocketClient]
    client      : Union[CMFutures, UMFutures]

    def load_from_env(type: FutureClientType) -> Self:
        load_dotenv()
        api_key, secret_key = load_key_from_env()
        return FutureClient(type, api_key, secret_key)

    def __init__(self, type: FutureClientType,  api_key : str, secret_key : str) -> None:
        if type == FutureClientType.COIN_M:
            self.client = CMFutures(key = api_key, secret = secret_key)
            self.ws_client = CMFuturesWebsocketClient()
        elif type == FutureClientType.USD_M:
            self.client = UMFutures(key = api_key, secret = secret_key)
            self.ws_client = UMFuturesWebsocketClient()
        else:
            raise Exception("Invalid Future Client Type!!")

    def get_available(self):
        return self.client.account()["availableBalance"]
    
    def get_open_positions(self):
        open_pos = filter(lambda p: float(p["positionAmt"]) != 0, self.client.account()["positions"])
        return dict((p['symbol'], p) for p in open_pos)
    
    def get_position(self, symbol : str):
        return filter(lambda p: p["symbol"] == symbol, self.client.account()['positions']).__next__()

    def order_limit(
            self, 
            symbol : str, 
            order_type: FutureOrderType, 
            price : float, 
            quantity : float, 
            leverage : Optional[int] = None, 
            margin_type : Optional[FutureMarginType] = None
        ):
        side = order_type.value
        type = "LIMIT"


        if margin_type != None: self.client.change_margin_type(symbol=symbol, marginType=margin_type.value)
        if leverage != None: self.client.change_leverage(symbol=symbol, leverage=leverage)
        return self.client.new_order(
            symbol = symbol, 
            side = side, 
            type = type, 
            timeInForce = "GTC",
            quantity = quantity,
            price = price
        )
    
    def order_market(
            self, 
            symbol : str, 
            order_type : FutureOrderType, 
            quantity : float, 
            leverage : Optional[int] = None, 
            margin_type: Optional[FutureMarginType] = None
        ):
        side = order_type.value
        type = "MARKET"

        if margin_type != None: self.client.change_margin_type(symbol=symbol, marginType=margin_type.value)
        if leverage != None: self.client.change_leverage(symbol=symbol, leverage=leverage)
        return self.client.new_order(
            symbol, 
            side = side, 
            type = type, 
            quantity = quantity
        )

def main():
    client = FutureClient.load_from_env(FutureClientType.USD_M)

    # client.client.change_leverage('XRPUSDT', 1)
    # client.order_market('XRPUSDT', order_type=FutureOrderType.SHORT, quantity=80, leverage=20)
if __name__ == '__main__':
    main()