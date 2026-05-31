import os
import pandas as pd
from get_nse_symbols import get_nse_symbols
from fii_dii_scraper import get_fii_dii_activity
from order_book_extractor import extract_order_book_from_pdf

# The 'batch_analyzer' module as previously written does not expose 'all_results', so we run it via subprocess
import subprocess

def run_all():
    print("=== 1. Fetching NSE symbols...")
    symbols = get_nse_symbols()
    print(f"Got {len(symbols)} symbols.")

    print("=== 2. Running batch analyzer for all companies...")
    # Run batch_analyzer.py as a subprocess
    subprocess.run(["python", "ideas/stock-market-analyzer/batch_analyzer.py"])  # Assumes current wd is repo root

    print("=== 3. Running FII/DII activity scraper...")
    get_fii_dii_activity()
    fii_dii_df = pd.read_csv("fii_dii_activity.csv")

    print("=== 4. Extracting Order Book info from PDFs...")
    report_folder = "ideas/stock-market-analyzer/annual_reports"
    orderbook_summaries = []
    if os.path.isdir(report_folder):
        for filename in os.listdir(report_folder):
            if filename.lower().endswith('.pdf'):
                extract_order_book_from_pdf(os.path.join(report_folder, filename))
                # Optionally process CSVs produced for summary
    else:
        print("No 'annual_reports' folder found; skipping order book extraction.")

    print("=== 5. Preparing common summary report...")
    if os.path.exists("nse_stock_analysis.csv"):
        df_metrics = pd.read_csv("nse_stock_analysis.csv")
    else:
        df_metrics = pd.DataFrame()

    output_path = "nse_stock_market_full_report.xlsx"
    with pd.ExcelWriter(output_path) as writer:
        if not df_metrics.empty:
            df_metrics.to_excel(writer, sheet_name="Stock Metrics", index=False)
        if not fii_dii_df.empty:
            fii_dii_df.to_excel(writer, sheet_name="FII_DII Activity", index=False)
        # Add more sheets as desired
    print(f"=== Finished! Combined report saved as: {output_path}")

if __name__ == "__main__":
    run_all()
