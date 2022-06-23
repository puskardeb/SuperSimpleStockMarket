import datetime

from controllers.datastore import DataStoreController
from controllers.dividend import DividendController
from controllers.pe_ratio import PERatioController
from controllers.trade_operations import TradeController
from controllers.volume_weighted import VolumeWeightedStockPriceController
from controllers.gbce import GBCEController


def run():
    DataStoreController.populate()
    menu_msg = "Please select an option as per choice:-\n" \
               "1 for calculating dividend yield.\n" \
               "2 for calculating P/E ratio.\n" \
               "3 for recording trade.\n" \
               "4 for calculating Volume Weighted Stock Price.\n" \
               "5 for calculating the GBCE All Share Index.\n" \
               "0 for exiting..." \

    stock_choice_list = set(DataStoreController.get_stock_list().keys())
    stock_choice_msg = "Enter a stock from {} :".format(stock_choice_list)
    SUCCESS, FAIL = "success", "fail"

    while True:
        try:
            print(menu_msg)
            option = int(input("Enter option:"))

            if option == 1:
                stock_name = input(stock_choice_msg).upper()
                price = float(input("Enter price:"))
                ret_str, value = DividendController.calculate(stock_name, price)
                if ret_str == SUCCESS:
                    print("Dividend yield for stock '{}' with price {} is {}".format(stock_name, price, value))
                else:
                    print("Unable to calculate dividend yield for '{}'".format(stock_name))
            elif option == 2:
                stock_name = input(stock_choice_msg).upper()
                price = float(input("Enter price:"))
                ret_str, value = PERatioController.calculate(stock_name, price)
                if ret_str == SUCCESS:
                    print("PE ratio for stock '{}' with price {} is {}.".format(stock_name, price, value))
                else:
                    print("Unable to calculate PE ratio for '{}'".format(stock_name))
            elif option == 3:
                stock_name = input(stock_choice_msg).upper()
                quantity = int(input("Enter quantity:"))
                price = float(input("Enter price:"))
                buy_or_sell = input("Enter 'BUY' or 'SELL':").upper()
                record_to_file = input("Do you want to record this trade to file? Type 'YES' or 'NO':")
                if record_to_file.strip().upper() not in ["YES", "NO"]:
                    print("Invalid choice selected! Please select either 'YES' or 'NO'.")
                    continue
                record_to_file = record_to_file.strip().upper() == "YES"
                ret_str = TradeController.record(stock_name, buy_or_sell, quantity, price, record_to_file)
                if ret_str == SUCCESS:
                    print("Recorded trade for {}ing stock '{}' with quantity {} and price {}".format(buy_or_sell.lower(), stock_name, quantity, price))
                else:
                    print("Failed to record trade!")
            elif option == 4:
                stock_name = input(stock_choice_msg).upper()
                minutes = datetime.timedelta(minutes=5)
                ret_str, value = VolumeWeightedStockPriceController.calculate(stock_name, minutes)
                if ret_str == SUCCESS:
                    print("Volume Weighted Stock Price for '{}' within the last {} minutes is {}.".format(stock_name, minutes, value))
                else:
                    print("Unable to calculate the volume weighted stock price for '{}'".format(stock_name))
            elif option == 5:
                ret_str, value = GBCEController.calculate()
                if ret_str == SUCCESS:
                    print("The GBCE All Share Index is {}.".format(value))
                else:
                    print("Unable to calculate GBCE All Share Index!")
            elif option == 0:
                TradeController.clear_file()
                break
            else:
                print("Invalid option. Please select between [0-5]")
        except ValueError as VE:
            print(VE)
        except UnboundLocalError as ULE:
            print(ULE)
        except Exception as ex:
            print(ex)
