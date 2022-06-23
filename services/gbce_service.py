import math

from controllers.volume_weighted import VolumeWeightedStockPriceController
from controllers.trade_operations import TradeController
from errors.error import InvalidValueError


class GBCEService:

    @staticmethod
    def calculate():
        trade_list = TradeController.get_trade_ledger()

        if not trade_list:
            raise InvalidValueError("No trades have been recorded yet!")

        total_vwsp = 1.0

        for stock in trade_list.keys():
            ret_str, vswp = VolumeWeightedStockPriceController.calculate(stock)
            if ret_str == "success":
                total_vwsp *= vswp

        gbce_all_share_index = math.pow(total_vwsp, 1 / len(trade_list))
        return gbce_all_share_index
