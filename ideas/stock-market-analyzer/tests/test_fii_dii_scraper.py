import unittest
import os
import pandas as pd
import importlib.util

class TestFiiDiiScraper(unittest.TestCase):
    def test_fii_dii_output(self):
        # Dynamically import and run scraper
        spec = importlib.util.spec_from_file_location("fii_dii_scraper", "ideas/stock-market-analyzer/fii_dii_scraper.py")
        fds = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(fds)
        # Output file expected
        self.assertTrue(os.path.exists("fii_dii_activity.csv"))
        df = pd.read_csv("fii_dii_activity.csv")
        self.assertTrue(df.shape[0] > 0)
        # Clean up
        os.remove("fii_dii_activity.csv")

if __name__ == "__main__":
    unittest.main()
