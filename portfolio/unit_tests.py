import unittest

from .import signals
from .signals import getStockPrice


class TestSignals(unittest.TestCase):

    def test_add(self):
        result = signals.add(10, 5)
        self.assertEqual(result, 15)
