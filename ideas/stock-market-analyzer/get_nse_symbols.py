import requests
import pandas as pd

def get_nse_symbols():
    # Download all equity securities from NSE (adjust URL if NSE updates layout)
    url = 'https://www1.nseindia.com/content/equities/EQUITY_L.csv'
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    with open('EQUITY_L.csv', 'w', encoding='utf-8') as f:
        f.write(r.text)
    df = pd.read_csv('EQUITY_L.csv')
    symbols = df['SYMBOL'].tolist()
    return symbols

if __name__ == "__main__":
    symbols = get_nse_symbols()
    print(symbols[:10])  # Preview
