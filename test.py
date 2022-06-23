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


if __name__ == '__main__':
    unittest.main()
