# sov_engine.py
from collections import defaultdict
from config import RANK_WEIGHTS, SENTIMENT_WEIGHT, SOURCE_WEIGHT

class ShareOfVoiceEngine:
    def compute(self, results):
        brand_scores = defaultdict(float)

        for r in results:
            rank_weight = RANK_WEIGHTS.get(r["rank"], 0.1)
            sentiment_factor = SENTIMENT_WEIGHT[r["sentiment"]]
            source_factor = SOURCE_WEIGHT[r["source_type"]]

            for brand, mentions in r["brand_mentions"].items():
                if mentions > 0:
                    effective_mentions = min(mentions, 3)
                    brand_scores[brand] += (
                        rank_weight
                        * effective_mentions
                        * sentiment_factor
                        * source_factor
                    )

        total = sum(brand_scores.values()) or 1.0
        return {
            brand: round((score / total)*100, 3)
            for brand, score in brand_scores.items()
        }
