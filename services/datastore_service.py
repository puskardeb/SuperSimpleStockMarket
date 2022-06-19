import os

import pandas as pd
from data_models.stocks import Stock


class DataStoreService:
    stock_list = dict()

    @staticmethod
    def get_stock_list():
        return DataStoreService.stock_list

    @staticmethod
    def populate():
        current_directory = os.getcwd()
        csv_file_location = os.path.join('files', 'gbce_stock_info.csv')
        full_path = os.path.join(current_directory, csv_file_location)
        print("Reading from {}...".format(full_path))

        stocks_dataframe = pd.read_csv(full_path)

        for index, stock_row in stocks_dataframe.iterrows():
            symbol, type, last_div, fixed_div, par_val = stock_row
            if fixed_div.strip() == '':
                fixed_div = 0.0

            stock = Stock(symbol=symbol.strip(),
                          type=type.strip(),
                          last_dividend=float(last_div),
                          fixed_dividend=float(fixed_div),
                          par_value=float(par_val))
            DataStoreService.stock_list[symbol] = stock

        # print(DataStoreService.stock_list)