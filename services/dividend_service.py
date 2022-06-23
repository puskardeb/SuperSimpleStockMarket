from controllers.datastore import DataStoreController
from data_models.stocks import Stock
from errors.error import InvalidValueError, StockTypeError


class DividendService:

    @staticmethod
    def calculate(stock, price):
        if price <= 0:
            raise InvalidValueError("Price is {} which is invalid.".format(price))

        stock = stock.upper()
        stock_list = DataStoreController.get_stock_list()
        stock_obj = stock_list[stock]
        stock_type = stock_obj.get_type().upper()

        if stock_type == Stock.COMMON:
            last_div = stock_obj.get_last_dividend()
            dividend = last_div / price
        elif stock_type == Stock.PREFERRED:
            fixed_div = stock_obj.get_fixed_dividend()
            par_value = stock_obj.get_par_value()
            dividend = (fixed_div * par_value) / price
        else:
            raise StockTypeError('Invalid stock type!')

        return dividend
