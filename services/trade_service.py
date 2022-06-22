import os

from data_models.trades import Trade
from errors.error import StockNotFoundError, InvalidValueError
from controllers.datastore import DataStoreController


class TradeService:
    trade_ledger = {}

    @staticmethod
    def get_trade_ledger():
        return TradeService.trade_ledger

    @staticmethod
    def record(stock, type, quantity, price, timestamp, dump_to_file):
        if stock not in DataStoreController.get_stock_list():
            raise StockNotFoundError("Invalid stock!")

        if type.strip().upper() not in ["BUY", "SELL"]:
            raise InvalidValueError("Invalid value! Need to enter either 'BUY' or 'SELL'!")

        trade = Trade(type, quantity, price, timestamp)

        if stock not in TradeService.trade_ledger:
            TradeService.trade_ledger[stock] = {}

        TradeService.trade_ledger[stock][timestamp] = trade

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
