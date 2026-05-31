# Stock Market Analyzer (`ideas/stock-market-analyzer`)

A modular toolkit for analyzing all stocks listed on the NSE (India) with a single click. It scrapes financial ratios, FII/DII activity, and recent order book news. Ideal for both comprehensive and independent, script-by-script usage.

---

## Features
- **Get and maintain all NSE equity symbols**
- **Batch download key financial metrics for all stocks** (PE, cash flow, operating margin, revenue growth)
- **Fetch and review FII/DII buy/sell activity**
- **Crawl web news for recent order book wins**
- **Single-click runner for end-to-end analysis and report**

---

## Quick Start: Single Click Full Analysis
1. Ensure you have Python 3.x and the required packages:
   ```bash
   pip install yfinance pandas requests beautifulsoup4 openpyxl
   # For optional PDF support: pip install camelot-py[cv]
   ```
2. To run the full analysis (all steps, unified Excel report):
   ```bash
   python ideas/stock-market-analyzer/run_full_analysis.py
   ```
   - Output: `nse_stock_market_full_report.xlsx` in the current folder

---

## Script-by-Script Usage

- **Get NSE Symbols:**
  ```bash
  python ideas/stock-market-analyzer/get_nse_symbols.py
  ```
- **Batch Analyzer (financials for all stocks):**
  ```bash
  python ideas/stock-market-analyzer/batch_analyzer.py
  ```
- **FII/DII Scraper:**
  ```bash
  python ideas/stock-market-analyzer/fii_dii_scraper.py
  ```
- **Order Book Web Crawler:**
  ```bash
  python ideas/stock-market-analyzer/order_book_webcrawler.py
  ```
    - Edit and expand the company slug list in the script to match your coverage

---

## Notes
- Some web sources may rate-limit or block excessive crawling; adjust delays as needed.
- All outputs are saved as CSV or Excel files.
- For corporate order book news, script currently works for select companies via Moneycontrol; expand logic for more coverage as needed.
- Contributions and improvements welcome (PR, issues)!

