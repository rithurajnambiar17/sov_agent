from collections import defaultdict
import re

class BrandAnalyzer:
    def __init__(self, brands):
        self.brands = brands

    def count_mentions(self, text: str):
        counts = defaultdict(int)
        for brand in self.brands:
            counts[brand] = len(
                re.findall(rf"\b{brand}\b", text)
            )
        return counts
