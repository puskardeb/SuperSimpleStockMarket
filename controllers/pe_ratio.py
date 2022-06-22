from services.pe_ratio_service import PERatioService
from errors.error import InvalidValueError


class PERatioController:

    @staticmethod
    def calculate(stock, price):
        try:
            return "success", PERatioService.calculate(stock, price)
        except KeyError:
            print("Stock '{}' not present in stock list".format(stock))
            return "fail", None
        except InvalidValueError as IVE:
            print(IVE)
            return "fail", None
