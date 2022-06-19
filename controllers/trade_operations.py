import datetime
from controllers.datastore import DataStoreController
from services.trade_service import TradeService

class TradeController:
    @staticmethod
    def get_trade_ledger():
        return TradeService.get_trade_ledger()

    @staticmethod
    def record(stock, type, quantity, price):
        if stock not in DataStoreController.get_stock_list():
            print("Invalid stock entered!")
            return
        TradeService.record(stock, type, quantity, price, datetime.datetime.now())