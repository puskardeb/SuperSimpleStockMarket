import datetime

from services.trade_service import TradeService

class TradeController:
    @staticmethod
    def get_trade_ledger():
        return TradeService.trade_ledger

    @staticmethod
    def record(stock, type, quantity, price):
        TradeService.record(stock, type, quantity, price, datetime.datetime.now())