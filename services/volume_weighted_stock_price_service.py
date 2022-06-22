import datetime

from controllers.trade_operations import TradeController
from controllers.datastore import DataStoreController
from errors.error import InvalidValueError, StockNotFoundError


class VolumeWeightedStockPriceService:

    @staticmethod
    def calculate(stock, before_time):
        if stock not in DataStoreController.get_stock_list():
            raise StockNotFoundError("Stock '{}' is not present in stock list. Please enter a correct stock!".format(stock))

        trade_dict = TradeController.get_trade_ledger()

        if stock not in trade_dict:
            raise StockNotFoundError("Trades of stock '{}' are not yet recorded!".format(stock))

        if before_time == datetime.datetime.min:
            diff_time = before_time
        else:
            diff_time = datetime.datetime.now() - before_time
        total_traded_quantity = 0
        total_price = 0

        for time, trade in trade_dict[stock].items():
            if time >= diff_time:
                traded_price = trade.get_price()
                traded_quantity = trade.get_quantity()

                total_traded_quantity += traded_quantity
                total_price += (traded_price * traded_quantity)

        if total_traded_quantity == 0:
            raise InvalidValueError('The quantity of trades recorded within the last {} minutes is {}.'.format(before_time, total_traded_quantity))

        return total_price / total_traded_quantity
