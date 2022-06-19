from services.pe_ratio_service import PERatioService


class PERatioController:

    @staticmethod
    def calculate(stock, price):
        try:
            return PERatioService.calculate(stock, price)
        except KeyError:
            print("Stock '{}' not present in stock list".format(stock))
            return -1
        except ZeroDivisionError:
            print("Calculated dividend came out to be 0. Returning PE ratio as 0.0")
            return 0.0
