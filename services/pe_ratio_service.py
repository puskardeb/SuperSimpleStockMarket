from controllers.dividend import DividendController
from errors.error import InvalidValueError


class PERatioService:

    @staticmethod
    def calculate(stock, price):
        ret_str, dividend = DividendController.calculate(stock, price)

        if ret_str == "success" and dividend == 0.0:
            raise InvalidValueError('Calculated dividend came out to be {} which is invalid.'.format(dividend))

        pe_ratio = price / dividend

        return pe_ratio
