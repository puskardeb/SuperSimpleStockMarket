import os

import pandas as pd
import pprint

from data_models.stocks import Stock
from errors.error import StockTypeError


class DataStoreService:
    stock_list = dict()

    @staticmethod
    def get_stock_list():
        return DataStoreService.stock_list

    @staticmethod
    def populate_from_csv():

        current_directory = os.getcwd()
        csv_file_location = os.path.join('files', 'gbce_stock_info.csv')
        full_path = os.path.join(current_directory, csv_file_location)

        stocks_dataframe = pd.read_csv(full_path)
        print("Reading from {}...".format(full_path))
        iter_rows = stocks_dataframe.iterrows()

        DataStoreService.populate(iter_rows)

    @staticmethod
    def populate_from_defaults():
        default_stock_info_map = DataStoreService.get_default_stock_info()
        pp = pprint.PrettyPrinter(depth=4)

        print("Reading from default stock info in memory ...")
        pp.pprint(default_stock_info_map)
        iter_rows = enumerate(default_stock_info_map)

        DataStoreService.populate(iter_rows)

    @staticmethod
    def populate(iter_rows):
        for index, stock_row in iter_rows:
            symbol, type, last_div, fixed_div, par_val = stock_row
            if fixed_div.strip() == '':
                fixed_div = 0.0

            if type.strip().upper() not in ['COMMON', 'PREFERRED']:
                raise StockTypeError('Invalid Stock Type!')

            stock = Stock(symbol=symbol.strip(),
                          type=type.strip(),
                          last_dividend=float(last_div),
                          fixed_dividend=float(fixed_div),
                          par_value=float(par_val))
            DataStoreService.stock_list[symbol] = stock

    @staticmethod
    def get_default_stock_info():
        stock_set = {
            ('TEA', 'common', '0', '', '100'),
            ('POP', 'common', '8', '', '100'),
            ('ALE', 'common', '23', '', '60'),
            ('GIN', 'preferred', '8', '2', '100'),
            ('JOE', 'common', '13', '', '250')
        }

        return stock_set
