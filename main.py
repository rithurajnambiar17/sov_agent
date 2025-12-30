import os
from config import KEYWORDS, BRANDS, TOP_N
from google_scraper import GoogleSearchClient
from content_fetcher import PageContentFetcher
from brand_analyzer import BrandAnalyzer
from sentiment import SentimentAnalyzer
from source_classifier import classify_source
from sov_engine import ShareOfVoiceEngine
import dotenv

dotenv.load_dotenv()

search_client = GoogleSearchClient(
    api_key=os.getenv("SERP_API_KEY")
)
fetcher = PageContentFetcher()
brand_analyzer = BrandAnalyzer(BRANDS)
sentiment_analyzer = SentimentAnalyzer()
sov_engine = ShareOfVoiceEngine()

for keyword in KEYWORDS:
    print(f"\n🔍 Keyword: {keyword}")
    organic_results = search_client.search(keyword, TOP_N)
    processed_results = []

    for idx, result in enumerate(organic_results, start=1):
        text = fetcher.fetch_text(result["link"])
        brand_mentions = brand_analyzer.count_mentions(text)
        sentiment = sentiment_analyzer.classify(text)
        source_type = classify_source(result["link"])
        print(
            f"Rank {idx} | {source_type} | "
            f"Atomberg mentions: {brand_mentions['atomberg']} | "
            f"Crompton mentions: {brand_mentions['crompton']}"
        )

        processed_results.append({
            "rank": idx,
            "url": result["link"],
            "source_type": source_type,
            "brand_mentions": brand_mentions,
            "sentiment": sentiment
        })

    sov = sov_engine.compute(processed_results)
    print("📊 Share of Voice:", sov)
