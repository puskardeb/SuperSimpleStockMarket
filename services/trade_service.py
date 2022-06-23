import os

from data_models.trades import Trade
from errors.error import StockNotFoundError, InvalidValueError
from controllers.datastore import DataStoreController


class TradeService:
    trade_ledger = {}

    @classmethod
    def get_trade_ledger(cls):
        return cls.trade_ledger

    @classmethod
    def record(cls, stock, type, quantity, price, timestamp, dump_to_file):
        if stock not in DataStoreController.get_stock_list():
            raise StockNotFoundError("Invalid stock!")

        if type.strip().upper() not in ["BUY", "SELL"]:
            raise InvalidValueError("Invalid value! Need to enter either 'BUY' or 'SELL'!")

        if price < 0:
            raise InvalidValueError("Invalid value for price! Price cannot have negative value!")

        if quantity < 0:
            raise InvalidValueError("Invalid value for quantity! Quantity cannot have negative value!")

        trade = Trade(type, quantity, price, timestamp)

        if stock not in cls.trade_ledger:
            cls.trade_ledger[stock] = {}

        cls.trade_ledger[stock][timestamp] = trade

        if dump_to_file:
            TradeService.write_to_file(stock, trade)

    @staticmethod
    def write_to_file(stock, trade):
        file_name = os.path.join('files', 'record_ledger.txt')

        with open(file_name, 'a') as f:
            f.writelines("{}, {}\n".format(stock, trade))

    @staticmethod
    def clear_file():
        file_name = os.path.join('files', 'record_ledger.txt')
        with open(file_name, 'w') as f:
            pass

    @classmethod
    def clear_records(cls):
        cls.trade_ledger = {}
