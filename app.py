from controllers.datastore import DataStoreController
from controllers.dividend import DividendController
from controllers.pe_ratio import PERatioController
from controllers.trade_operations import TradeController
from controllers.volume_weighted import VolumeWeightedStockPriceController


def run():
    DataStoreController.populate()
    menu_msg = "1 for Calculating DIVIDEND yield.\n" \
               "2 for calculating P/E ratio.\n" \
               "3 for Recording Trade.\n" \
               "4 for Calculating Volume Weighted Stock Price.\n" \
               "5 for Calculating the GBCE All Share Index.\n" \

    stock_choice_list = set(DataStoreController.get_stock_list().keys())
    stock_choice_msg = "Enter a stock from {} :".format(stock_choice_list)

    while True:
        stock_name = input(stock_choice_msg).upper()

        if stock_name == 'EXIT':
            break
        elif stock_name not in stock_choice_list:
            print("Invalid Stock")
            continue


        print(menu_msg)
        option = int(input("Enter option:"))
        if option == 1:
            price = float(input("Enter price:"))
            print(DividendController.calculate(stock_name, price))
        elif option == 2:
            price = float(input("Enter price:"))
            print(PERatioController.calculate(stock_name, price))
        elif option == 3:
            quantity = int(input("Enter quantity:"))
            price = float(input("Enter price:"))
            buy_or_sell = input("Enter 'BUY' or 'SELL':").upper()
            print(TradeController.record(stock_name, buy_or_sell, quantity, price))
        elif option == 4:
            print(VolumeWeightedStockPriceController.calculate(stock_name))
        elif option == 5:
            pass
        else:
            print("Invalid option. Please select between [0-4]")
        pass
