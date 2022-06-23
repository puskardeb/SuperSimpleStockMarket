import datetime

from controllers.datastore import DataStoreController
from services.trade_service import TradeService
from errors.error import StockNotFoundError, InvalidValueError


class TradeController:

    @staticmethod
    def process_record_trade_opt():
        stock_choice_list = set(DataStoreController.get_stock_list().keys())
        stock_choice_msg = "Enter a stock from {} :".format(stock_choice_list)
        stock_name = input(stock_choice_msg).upper()
        quantity = int(input("Enter quantity:"))
        price = float(input("Enter price:"))
        buy_or_sell = input("Enter 'BUY' or 'SELL':").upper()
        record_to_file = input("Do you want to record this trade to file? Type 'YES' or 'NO':")
        if record_to_file.strip().upper() not in ["YES", "NO"]:
            raise InvalidValueError("Invalid choice selected! Please select either 'YES' or 'NO'.")
        record_to_file = record_to_file.strip().upper() == "YES"
        ret_str = TradeController.record(stock_name, buy_or_sell, quantity, price, record_to_file)
        if ret_str == "success":
            print("Recorded trade for {}ing stock '{}' with quantity {} and price {}".format(buy_or_sell.lower(),
                                                                                             stock_name, quantity,
                                                                                             price))
        else:
            print("Failed to record trade!")

    @staticmethod
    def get_trade_ledger():
        return TradeService.get_trade_ledger()

    @staticmethod
    def record(stock, type, quantity, price, dump_to_file=True):
        try:
            TradeService.record(stock, type, quantity, price, datetime.datetime.now(), dump_to_file)
            return "success"
        except StockNotFoundError as SNFE:
            print(SNFE)
            return "fail"
        except Exception as ex:
            print(ex)
            return "fail"

    @staticmethod
    def clear_file():
        TradeService.clear_file()

    @staticmethod
    def clear_records():
        TradeService.clear_records()