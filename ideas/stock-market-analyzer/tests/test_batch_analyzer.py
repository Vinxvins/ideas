import unittest
import os
import pandas as pd
import importlib.util

class TestBatchAnalyzer(unittest.TestCase):
    def test_batch_analyzer_output(self):
        # Dynamically import batch_analyzer and run main logic
        spec = importlib.util.spec_from_file_location("batch_analyzer", "ideas/stock-market-analyzer/batch_analyzer.py")
        ba = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ba)
        # Should create output file:
        self.assertTrue(os.path.exists("nse_stock_analysis.csv"))
        df = pd.read_csv("nse_stock_analysis.csv")
        self.assertTrue('symbol' in df.columns)
        self.assertTrue(len(df) > 0)
        # Clean up
        os.remove("nse_stock_analysis.csv")

if __name__ == "__main__":
    unittest.main()
