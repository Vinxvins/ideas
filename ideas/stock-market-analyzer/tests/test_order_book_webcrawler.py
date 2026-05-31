import unittest
from order_book_webcrawler import get_order_book

class TestOrderBookWebcrawler(unittest.TestCase):
    def test_basic_extraction(self):
        results = get_order_book("larsen-toubro")
        self.assertIsInstance(results, list)
        for headline in results:
            self.assertIsInstance(headline, str)

if __name__ == "__main__":
    unittest.main()
