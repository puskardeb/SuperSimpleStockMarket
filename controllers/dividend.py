from controllers.datastore import DataStoreController
from services.dividend_service import DividendService
from errors.error import InvalidValueError


class DividendController:

    @staticmethod
    def process_dividend_opt():
        stock_choice_list = set(DataStoreController.get_stock_list().keys())
        stock_choice_msg = "Enter a stock from {} :".format(stock_choice_list)
        stock_name = input(stock_choice_msg)
        price = float(input("Enter price:"))
        ret_str, value = DividendController.calculate(stock_name, price)
        if ret_str == "success":
            print("Dividend yield for stock '{}' with price {} is {}".format(stock_name, price, value))
        else:
            print("Unable to calculate dividend yield for '{}'".format(stock_name))

    @staticmethod
    def calculate(stock, price):
        try:
            return "success", DividendService.calculate(stock, price)
        except KeyError:
            print("Stock '{}' not present in stock list".format(stock))
            return "fail", None
        except InvalidValueError as IVE:
            print(IVE)
            return "fail", None
        except Exception as ex:
            print(ex)
            return "fail", None
