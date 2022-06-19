import math

from controllers.volume_weighted import VolumeWeightedStockPriceController
from controllers.trade_operations import TradeController


class GBCEService:

    @staticmethod
    def calculate():
        trade_list = TradeController.get_trade_ledger()

        total_vwsp = 0
        for stock, values in trade_list.keys():
            total_vwsp += VolumeWeightedStockPriceController.calculate(stock)

        gbce_all_share_index = math.pow(total_vwsp, 1 / len(trade_list))
        return gbce_all_share_index
