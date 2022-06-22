import datetime
from services.trade_service import TradeService
from errors.error import StockNotFoundError


class TradeController:
    @staticmethod
    def get_trade_ledger():
        return TradeService.get_trade_ledger()

    @staticmethod
    def record(stock, type, quantity, price, dump_to_file=True):
        try:
            TradeService.record(stock, type, quantity, price, datetime.datetime.now(), dump_to_file)
            return "success"
        except StockNotFoundError as SNFE:
            print(SNFE)
            return "fail"

    @staticmethod
    def clear_file():
        TradeService.clear_file()