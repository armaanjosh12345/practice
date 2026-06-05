import requests
import os
from datetime import datetime, timedelta

class DataCollector:
    def __init__(self, news_api_key=None, fred_api_key=None):
        self.news_api_key = news_api_key or os.getenv("NEWSAPI_KEY")
        self.fred_api_key = fred_api_key or os.getenv("FRED_API_KEY")

    def get_news_sentiment(self, query="forex gold"):
        if not self.news_api_key:
            return "News API key missing"

        url = "https://newsapi.org/v2/everything"
        params = {
            "q": query,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 10,
            "apiKey": self.news_api_key
        }
        try:
            response = requests.get(url, params=params)
            articles = response.json().get('articles', [])
            return [a['title'] for a in articles]
        except Exception as e:
            return f"Error fetching news: {str(e)}"

    def get_macro_data(self, series_id="FEDFUNDS"):
        if not self.fred_api_key:
            return "FRED API key missing"

        url = "https://api.stlouisfed.org/fred/series/observations"
        params = {
            "series_id": series_id,
            "api_key": self.fred_api_key,
            "file_type": "json",
            "limit": 1,
            "sort_order": "desc"
        }
        try:
            response = requests.get(url, params=params)
            observations = response.json().get('observations', [])
            if observations:
                return observations[0]['value']
            return "No data"
        except Exception as e:
            return f"Error fetching macro: {str(e)}"

    def get_all_context(self):
        return {
            "news": self.get_news_sentiment(),
            "fed_rates": self.get_macro_data("FEDFUNDS"),
            "inflation": self.get_macro_data("CPIAUCSL")
        }
