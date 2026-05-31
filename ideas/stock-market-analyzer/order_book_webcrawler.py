import requests
from bs4 import BeautifulSoup
import time

def get_order_book(company_slug):
    # Example: company_slug = 'larsen-toubro' (for L&T)
    url = f"https://www.moneycontrol.com/company-article/{company_slug}/news/{company_slug}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    ob_news = []
    for story in soup.find_all("div", class_="FL"):
        text = story.get_text(strip=True)
        if "order book" in text.lower() or "order win" in text.lower():
            ob_news.append(text)
    return ob_news

if __name__ == "__main__":
    companies = ["larsen-toubro", "bhel", "bharat-electronics"]
    results = {}
    for comp in companies:
        result = get_order_book(comp)
        print(f"{comp}: {result}")
        results[comp] = result
        time.sleep(2) # Avoid hitting servers too rapidly
