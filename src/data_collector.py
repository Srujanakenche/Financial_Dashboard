import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

def fetch_stock_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    """Fetches historical stock data using yfinance."""
    print(f"Fetching data for {ticker}...")
    df = yf.download(ticker, period=period)
    df.reset_index(inplace=True)
    return df

def fetch_stock_news(ticker_name: str) -> list:
    """Scrapes recent news headlines for a given company name using Google News RSS."""
    print(f"Scraping news headlines for {ticker_name}...")
    url = f"https://news.google.com/rss/search?q={ticker_name}+stock&hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="xml")
    
    news_items = []
    items = soup.find_all('item')[:10] # Limit to top 10 recent articles
    
    for item in items:
        news_items.append({
            'title': item.title.text,
            'pub_date': item.pubDate.text,
            'source': item.source.text
        })
    return news_items