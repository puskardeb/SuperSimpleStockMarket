import datetime
import unittest
from controllers.datastore import DataStoreController
from controllers.dividend import DividendController
from controllers.pe_ratio import PERatioController
from controllers.trade_operations import TradeController
from controllers.volume_weighted import VolumeWeightedStockPriceController
from controllers.gbce import GBCEController


class TestCase(unittest.TestCase):
    def test_dividend(self):
        DataStoreController.populate()
        ret_str1, value1 = DividendController.calculate('TEA', 98)
        ret_str2, value2 = DividendController.calculate('ALE', 8)
        ret_str3, value3 = DividendController.calculate('gIn', 1)
        ret_str4, value4 = DividendController.calculate('KOL', 4.5)
        ret_str5, value5 = DividendController.calculate('JOE', -98.0)
        ret_str6, value6 = DividendController.calculate(980, 83)

        self.assertEqual(value1, 0.0)
        self.assertEqual(value2, 2.875)
        self.assertEqual(value3, 2.0)
        self.assertEqual(value4, None)
        self.assertEqual(value5, None)
        self.assertEqual(value6, None)

    def test_pe_ratio(self):
        DataStoreController.populate()

        ret_str1, value1 = PERatioController.calculate('TEA', 76)
        ret_str2, value2 = PERatioController.calculate('ALE', 0.65)
        ret_str3, value3 = PERatioController.calculate('gIn', 14)
        ret_str4, value4 = PERatioController.calculate('KOL', -8.5)
        ret_str5, value5 = PERatioController.calculate('JOE', 8.0)
        ret_str6, value6 = PERatioController.calculate(float('inf'), float('-inf'))

        self.assertEqual(value1, None)
        self.assertEqual(value2, 0.018369565217391304)
        self.assertEqual(value3, 98.0)
        self.assertEqual(value4, None)
        self.assertEqual(value5, 4.923076923076923)
        self.assertEqual(value6, None)

    def test_record_trade(self):
        ret_str1 = TradeController.record('ALE', 'buy', 4, 5, True)
        ret_str2 = TradeController.record('KOL', 'sell', 9, 0, True)
        ret_str3 = TradeController.record('JOE', 'BUY', 7, 9, False)
        ret_str4 = TradeController.record(98, 'preferred', -1, 8, False)
        ret_str5 = TradeController.record('tEa', 1, 1, -1, True)
        ret_str6 = TradeController.record('GIN', 'sell', 0, 0, True)

        self.assertEqual(ret_str1, "success")
        self.assertEqual(ret_str2, "fail")
        self.assertEqual(ret_str3, "success")
        self.assertEqual(ret_str4, "fail")
        self.assertEqual(ret_str5, "fail")
        self.assertEqual(ret_str6, "success")

        TradeController.clear_records()

    def test_volume_weighted(self):
        TradeController.record('ALE', 'SELL', 9, 10, True)
        TradeController.record('GIN', 'SELL', 5, 7, False)
        TradeController.record('ALE', 'BUY', 89, 190, False)
        TradeController.record('TEA', 'SELL', 2.9, 1.1, True)

        ret_str1, value1 = VolumeWeightedStockPriceController.calculate('ALE', datetime.timedelta(minutes=5))
        ret_str2, value2 = VolumeWeightedStockPriceController.calculate('POP', datetime.timedelta(minutes=5))
        ret_str3, value3 = VolumeWeightedStockPriceController.calculate('GIN', datetime.timedelta(minutes=5))
        ret_str4, value4 = VolumeWeightedStockPriceController.calculate('IGN', datetime.timedelta(minutes=5))
        ret_str5, value5 = VolumeWeightedStockPriceController.calculate('TEA', datetime.timedelta(minutes=5))
        ret_str6, value6 = VolumeWeightedStockPriceController.calculate('FAT', -1)

        self.assertEqual(value1, 173.46938775510205)
        self.assertEqual(value2, None)
        self.assertEqual(value3, 7.0)
        self.assertEqual(value4, None)
        self.assertEqual(value5, None)
        self.assertEqual(value6, None)

        TradeController.clear_records()

    def test_gbce(self):
        TradeController.record('ALE', 'SELL', 9, 10, True)

        ret_str1, value1 = GBCEController.calculate()

        TradeController.record('GIN', 'SELL', 5, 7, False)
        TradeController.record('ALE', 'BUY', 89, 190, False)
        TradeController.record('TEA', 'SELL', 2.9, 1.1, True)

        ret_str2, value2 = GBCEController.calculate()

        TradeController.record('ABc', 'SELL', 4, 78.5, True)

        ret_str3, value3 = GBCEController.calculate()

        self.assertEqual(value1, 10.0)
        self.assertEqual(value2, 34.84660262185848)
        self.assertEqual(value3, 34.84660262185848)

        TradeController.clear_records()


if __name__ == '__main__':
    unittest.main()
