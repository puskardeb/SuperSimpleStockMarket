from controllers.datastore import DataStoreController
from data_models.stocks import Stock

class DividendService:
    def __init__(self):
        pass

    @staticmethod
    def calculate(stock, price):
        stock_list = DataStoreController.get_stock_list()
        stock_obj = stock_list[stock]
        stock_type = stock_obj.get_type().upper()
        dividend = None

        if stock_type == Stock.COMMON:
            last_div = stock_obj.get_last_dividend()
            dividend = last_div / price
        elif stock_type == Stock.PREFERRED:
            fixed_div = stock_obj.get_fixed_dividend()
            par_value = stock_obj.get_par_value()
            dividend = (fixed_div * par_value) / price

        return dividend
