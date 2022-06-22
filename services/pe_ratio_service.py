from controllers.dividend import DividendController
from errors.error import InvalidValueError


class PERatioService:

    @staticmethod
    def calculate(stock, price):
        dividend = DividendController.calculate(stock, price)

        if dividend <= 0:
            raise InvalidValueError('Calculated dividend came out to be {} which is invalid.'.format(dividend))

        pe_ratio = price / dividend

        return pe_ratio
