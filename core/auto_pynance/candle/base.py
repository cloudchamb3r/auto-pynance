from auto_pynance import MarketType


class Base:
    @staticmethod
    def open(market :MarketType, symbol : str, index : int  = 0, interval : int = 1):
        ...
    @staticmethod
    def close(market :MarketType, symbol : str, index : int  = 0, interval : int = 1):
        ...
    @staticmethod
    def low(market :MarketType, symbol : str, index : int  = 0, interval : int = 1):
        ...
    @staticmethod
    def high(market :MarketType, symbol : str, index : int  = 0, interval : int = 1):
        ...
    @staticmethod
    def volume(market :MarketType, symbol : str, index : int  = 0, interval : int = 1):
        ...