import unittest
from stock_market_analyzer import Analyzer  # Assuming the main class is named Analyzer

class TestAnalyzer(unittest.TestCase):

    def test_data_fetching(self):
        analyzer = Analyzer()
        data = analyzer.fetch_data()  # Assuming fetch_data() is a method in Analyzer
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0, "Data fetched should not be empty")

    def test_metric_calculations(self):
        analyzer = Analyzer()
        metrics = analyzer.calculate_metrics([100, 200, 300])  # Example data
        self.assertIn('average', metrics)
        self.assertEqual(metrics['average'], 200, "Average should be correct")

    def test_recommendation_logic(self):
        analyzer = Analyzer()
        recommendation = analyzer.get_recommendation(300)  # Replace with appropriate test case
        self.assertIn(recommendation, ['buy', 'sell', 'hold'], "Recommendation should be one of buy, sell, or hold")

    def test_edge_cases(self):
        analyzer = Analyzer()
        # Edge case with empty data
        metrics = analyzer.calculate_metrics([])
        self.assertEqual(metrics, {'average': 0}, "Average should be 0 for no data")
        # Edge case with single data point
        metrics = analyzer.calculate_metrics([100])
        self.assertEqual(metrics['average'], 100, "Average should be equal to the single data point")

if __name__ == '__main__':
    unittest.main()