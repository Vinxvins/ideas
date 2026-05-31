import yfinance as yf
import pandas as pd
from get_nse_symbols import get_nse_symbols

symbols = get_nse_symbols()

all_results = []

for sym in symbols:
    ticker = f"{sym}.NS"
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        if info.get("regularMarketPrice"):
            all_results.append({
                "symbol": sym,
                "pe_ratio": info.get("trailingPE"),
                "operating_margin": info.get("operatingMargins"),
                "cash_flow": info.get("freeCashflow"),
                "revenue_growth": info.get("revenueGrowth"),
            })
    except Exception as e:
        print(f"Error fetching {sym}: {e}")

df = pd.DataFrame(all_results)
df.to_csv("nse_stock_analysis.csv", index=False)
print(f"Saved analysis for {len(all_results)} stocks.")
