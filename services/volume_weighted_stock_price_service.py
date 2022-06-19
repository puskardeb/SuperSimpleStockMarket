import datetime

from controllers.trade_operations import TradeController


class VolumeWeightedStockPriceService:
    @staticmethod
    def calculate(stock, before_time):
        trade_dict = TradeController.get_trade_ledger()
        if before_time == datetime.datetime.min:
            diff_time = before_time
        else:
            diff_time = datetime.datetime.now() - before_time
        total_traded_quantity = 0
        total_price = 0

        for time, trade in trade_dict[stock].items():
            if time >= diff_time:
                traded_price = trade.get_price()
                traded_quantity = trade.get_quantity()

                total_traded_quantity += traded_quantity
                total_price += (traded_price * traded_quantity)

        return total_price / total_traded_quantity
