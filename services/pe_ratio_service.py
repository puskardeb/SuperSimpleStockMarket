from controllers.dividend import DividendController


class PERatioService:
    def __init__(self):
        pass

    @staticmethod
    def calculate(stock, price):
        dividend = DividendController.calculate(stock, price)
        pe_ratio = price / dividend

        return pe_ratio
