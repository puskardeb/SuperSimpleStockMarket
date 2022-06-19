import datetime

from controllers.datastore import DataStoreController
from controllers.dividend import DividendController
from controllers.pe_ratio import PERatioController
from controllers.trade_operations import TradeController
from controllers.volume_weighted import VolumeWeightedStockPriceController
from controllers.gbce import GBCEController


def run():
    DataStoreController.populate()
    menu_msg = "1 for Calculating DIVIDEND yield.\n" \
               "2 for calculating P/E ratio.\n" \
               "3 for Recording Trade.\n" \
               "4 for Calculating Volume Weighted Stock Price.\n" \
               "5 for Calculating the GBCE All Share Index.\n" \
               "0 for exiting..." \

    stock_choice_list = set(DataStoreController.get_stock_list().keys())
    stock_choice_msg = "Enter a stock from {} :".format(stock_choice_list)

    while True:
        print(menu_msg)
        option = int(input("Enter option:"))

        if option == 1:
            stock_name = input(stock_choice_msg).upper()
            price = float(input("Enter price:"))
            print(DividendController.calculate(stock_name, price))
        elif option == 2:
            stock_name = input(stock_choice_msg).upper()
            price = float(input("Enter price:"))
            print(PERatioController.calculate(stock_name, price))
        elif option == 3:
            stock_name = input(stock_choice_msg).upper()
            quantity = int(input("Enter quantity:"))
            price = float(input("Enter price:"))
            buy_or_sell = input("Enter 'BUY' or 'SELL':").upper()
            print(TradeController.record(stock_name, buy_or_sell, quantity, price))
        elif option == 4:
            stock_name = input(stock_choice_msg).upper()
            print(VolumeWeightedStockPriceController.calculate(stock_name, datetime.timedelta(minutes=5)))
        elif option == 5:
            print(GBCEController.calculate())
        elif option == 0:
            break
        else:
            print("Invalid option. Please select between [0-5]")
        pass
