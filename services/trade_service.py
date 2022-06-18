from data_models.trades import Trade


class TradeService:
    trade_ledger = {}

    @staticmethod
    def record(stock, type, quantity, price, timestamp):
        trade = Trade(type, quantity, price, timestamp)

        if stock not in TradeService.trade_ledger:
            TradeService.trade_ledger[stock] = {}

        TradeService.trade_ledger[stock][timestamp] = trade
