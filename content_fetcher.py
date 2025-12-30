import requests
from bs4 import BeautifulSoup

class PageContentFetcher:
    def fetch_text(self, url: str) -> str:
        try:
            resp = requests.get(url, timeout=10, headers={
                "User-Agent": "Mozilla/5.0"
            })
            soup = BeautifulSoup(resp.text, "html.parser")

            for tag in soup(["script", "style", "noscript"]):
                tag.extract()

            text = " ".join(soup.stripped_strings)

            return text.lower()
        except Exception:
            return ""
