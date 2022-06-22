import datetime

from services.volume_weighted_stock_price_service import VolumeWeightedStockPriceService
from errors.error import InvalidValueError, StockNotFoundError


class VolumeWeightedStockPriceController:
    @staticmethod
    def calculate(stock, diff_time=datetime.datetime.min):
        try:
            return "success", VolumeWeightedStockPriceService.calculate(stock, diff_time)
        except StockNotFoundError as SNFE:
            print(SNFE)
            return "fail", None
        except InvalidValueError as IVE:
            print(IVE)
            return "fail", None
