from services.dividend_service import DividendService
from errors.error import InvalidValueError


class DividendController:

    @staticmethod
    def calculate(stock, price):
        try:
            return DividendService.calculate(stock, price)
        except KeyError:
            print("Stock '{}' not present in stock list".format(stock))
        except InvalidValueError as IVE:
            print(IVE)
