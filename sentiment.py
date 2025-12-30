# sentiment.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def classify(self, text: str):
        score = self.analyzer.polarity_scores(text)["compound"]
        if score >= 0.05:
            return "positive"
        elif score <= -0.05:
            return "negative"
        return "neutral"
