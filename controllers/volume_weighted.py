from services.volume_weighted_stock_price_service import VolumeWeightedStockPriceService


class VolumeWeightedStockPriceController:
    @staticmethod
    def calculate(stock):
        return VolumeWeightedStockPriceService.calculate(stock)
