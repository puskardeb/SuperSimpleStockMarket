from services.dividend_service import DividendService

class DividendController:
    def __init__(self):
        pass

    @staticmethod
    def calculate(stock, price):
        return DividendService.calculate(stock, price)