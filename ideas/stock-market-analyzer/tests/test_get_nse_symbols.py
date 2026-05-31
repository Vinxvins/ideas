import unittest
from get_nse_symbols import get_nse_symbols

class TestGetNseSymbols(unittest.TestCase):
    def test_output_is_list_and_nonempty(self):
        symbols = get_nse_symbols()
        self.assertIsInstance(symbols, list)
        self.assertTrue(len(symbols) > 0)
        self.assertTrue(all(isinstance(s, str) for s in symbols))

if __name__ == "__main__":
    unittest.main()
