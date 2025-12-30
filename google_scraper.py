from serpapi import GoogleSearch
import os

class GoogleSearchClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(self, query: str, top_n: int = 10):
        params = {
            "q": query,
            "engine": "google",
            "num": top_n,
            "api_key": self.api_key,
            "location" : "Hyderabad",
            "gl" : "IN"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        return results.get("organic_results", [])
