# source_classifier.py

def classify_source(url: str) -> str:
    url = url.lower()

    if any(domain in url for domain in ["amazon.", "croma.com", "flipkart."]):
        return "marketplace"

    if any(domain in url for domain in [
        "atomberg.com",
        "crompton.co.in",
        "orientelectric.com",
        "bajajelectricals.com"
    ]):
        return "brand_site"

    return "editorial"
