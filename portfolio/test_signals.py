import unittest
import signals
from portfolio.models import Stock, Portfolio

class TestCurrentPrice(unittest.TestCase):
    def test_getStockPrice(self):
        result = signals.getCurrentPrice('AIB')
        self.assertIsNot(type(result), type('string'))

        self.assertEquals(signals.add(10, 5), 15)

    def test_getCurrentPrice(self):
        result = signals.getCurrentPrice('AIB')
        self.assertIsNot(result), type(2)


    def test_getCurrentPrice(self):
        result = signals.getCurrentPrice('AIB')
        self.assertIs(type(result), type(1.23))


# class TestMovingAverage(unittest.TestCase):
#     def test_getStockPrice(self):
#         result = signals.getMovingAverage('AIB')
#         self.assertEquals(result, 15)
#
#         self.assertEquals(signals.add(10, 5), 15)
#
#     def test_getCurrentPrice(self):
#         result = signals.getMovingAverage('AIB')
#         self.assertEquals(result, 15)
#
#         self.assertEquals(signals.add(10, 5), 15)

class TestStockHigh(unittest.TestCase):
    def getStockHigh(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)
    def test_add(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)

class TestStockLow(unittest.TestCase):
    def test_add(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)

    def test_add(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)

class TestStockOpen(unittest.TestCase):
    def test_add(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)

    def test_add(self):
        result = signals.add(10, 5)
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)

class TestStockClose(unittest.TestCase):
    def test_add(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)

    def test_add(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)


class TestStockVolume(unittest.TestCase):
    def test_add(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)

    def test_add(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)


class TestUpdateStockPrice(unittest.TestCase):
    def test_add(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)

    def test_add(self):
        result = signals.getCurrentPrice('AIB')
        self.assertEquals(result, 15)

        self.assertEquals(signals.add(10, 5), 15)

if __name__ == '__main__':
    unittest.main()