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
               "0 for exiting and clearing the trade record ledger." \

    options_dict = {
        0: TradeController.clear_file,
        1: DividendController.process_dividend_opt,
        2: PERatioController.process_pe_ratio_opt,
        3: TradeController.process_record_trade_opt,
        4: VolumeWeightedStockPriceController.process_volume_weighted_stock_price_opt,
        5: GBCEController.process_gbce_opt
    }

    while True:
        try:
            print(menu_msg)
            option = int(input("Enter option:"))

            option_function = options_dict[option]
            option_function()

            if option not in options_dict.keys():
                print("Invalid option. Please select between [0-5]")
            elif option == 0:
                break

        except ValueError as VE:
            print(VE)

        except UnboundLocalError as ULE:
            print(ULE)

        except Exception as ex:
            print(ex)

