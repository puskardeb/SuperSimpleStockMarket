import datetime

from controllers.datastore import DataStoreController
from services.volume_weighted_stock_price_service import VolumeWeightedStockPriceService


class VolumeWeightedStockPriceController:
    @staticmethod
    def calculate(stock, diff_time=datetime.datetime.min):
        if stock not in DataStoreController.get_stock_list():
            print("Invalid stock!")
            return -1.0
        try:
            return VolumeWeightedStockPriceService.calculate(stock, diff_time)
        except KeyError:
            return 0.0
        except ZeroDivisionError:
            print("Total quantity in ledger is 0")
            return -1.0
