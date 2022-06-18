from controllers.datastore_controller import DataStoreController
from controllers.dividend import DividendController


def run():
    DataStoreController.populate()
    menu_msg = "1 for Calculating DIVIDEND yield.\n" \
               "2 for calculating P/E ratio.\n" \
               "3 for Recording Trade.\n" \
               "4 for Calculating Volume Weighted Stock Price.\n" \
               "5 for Calculating the GBCE All Share Index.\n" \
               "0 to exit, if you are done with all the operations.\n"

    stock_choice_list = list(DataStoreController.get_stock_list().keys())
    stock_choice_msg = "Enter a stock from {} :".format(stock_choice_list)

    while True:
        stock_name = input(stock_choice_msg).upper()
        print("Selected stock : {}".format(stock_name))
        print(menu_msg)
        option = int(input("Enter option:"))
        if option == 1:
            DividendController.calculate_dividend(stock_name)
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 0:
            break
        else:
            print("Invalid option. Please select between [0-5]")
        pass
