from controllers.datastore import DataStoreController
from services.pe_ratio_service import PERatioService
from errors.error import InvalidValueError


class PERatioController:

    @staticmethod
    def process_pe_ratio_opt():
        stock_choice_list = set(DataStoreController.get_stock_list().keys())
        stock_choice_msg = "Enter a stock from {} :".format(stock_choice_list)
        stock_name = input(stock_choice_msg).upper()
        price = float(input("Enter price:"))
        ret_str, value = PERatioController.calculate(stock_name, price)
        if ret_str == "success":
            print("PE ratio for stock '{}' with price {} is {}.".format(stock_name, price, value))
        else:
            print("Unable to calculate PE ratio for '{}'".format(stock_name))

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
