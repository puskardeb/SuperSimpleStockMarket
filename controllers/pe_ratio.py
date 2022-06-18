from services.pe_ratio_service import PERatioService

class PERatioController:
    def __init__(self):
        pass


    @staticmethod
    def calculate(stock, price):
        return PERatioService.calculate(stock, price)