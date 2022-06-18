import datetime

from controllers.trade_operations import TradeController


class VolumeWeightedStockPriceService:
    @staticmethod
    def calculate(stock):
        trade_dict = TradeController.get_trade_ledger()
        time_before_5_mins = datetime.datetime.now() - datetime.timedelta(minutes=5)
        total_traded_quantity = 0
        total_price = 0

        for time, trade in trade_dict[stock].items():
            if time >= time_before_5_mins:
                traded_price = trade.get_price()
                traded_quantity = trade.get_quantity()

                total_traded_quantity += traded_quantity
                total_price += (traded_price * traded_quantity)

        return total_price / total_traded_quantity
