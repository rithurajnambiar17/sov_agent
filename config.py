KEYWORDS = [
    "smart fan",
    "smart ceiling fan",
    "bldc smart fan"
]

BRANDS = [
    "atomberg",
    "havells",
    "crompton",
    "orient",
    "usha"
]

TOP_N = 10

RANK_WEIGHTS = {
    1: 1.0, 2: 0.9, 3: 0.8, 4: 0.7, 5: 0.6,
    6: 0.5, 7: 0.4, 8: 0.3, 9: 0.2, 10: 0.1
}

SENTIMENT_WEIGHT = {
    "positive": 1.2,
    "neutral": 1.0,
    "negative": 0.5
}

SOURCE_WEIGHT = {
    "marketplace": 1.0,
    "brand_site": 1.3,
    "editorial": 1.2
}
