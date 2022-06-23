import datetime

from controllers.datastore import DataStoreController
from services.volume_weighted_stock_price_service import VolumeWeightedStockPriceService
from errors.error import InvalidValueError, StockNotFoundError


class VolumeWeightedStockPriceController:

    @staticmethod
    def process_volume_weighted_stock_price_opt():
        stock_choice_list = set(DataStoreController.get_stock_list().keys())
        stock_choice_msg = "Enter a stock from {} :".format(stock_choice_list)
        stock_name = input(stock_choice_msg).upper()
        minutes = datetime.timedelta(minutes=5)
        ret_str, value = VolumeWeightedStockPriceController.calculate(stock_name, minutes)
        if ret_str == "success":
            print("Volume Weighted Stock Price for '{}' within the last {} minutes is {}.".format(stock_name, minutes,
                                                                                                  value))
        else:
            print("Unable to calculate the volume weighted stock price for '{}'".format(stock_name))

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
        except Exception as ex:
            print(ex)
            return "fail", None
