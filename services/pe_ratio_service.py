from controllers.dividend import DividendController


class PERatioService:

    @staticmethod
    def calculate(stock, price):
        dividend = DividendController.calculate(stock, price)
        pe_ratio = price / dividend

        return pe_ratio
