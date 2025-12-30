# **Share of Voice (SoV) Analysis – Smart Fan Category**

This project measures **Share of Voice (SoV)** for brands in the *smart fan* category using search-driven signals. It analyzes Google search results to quantify brand visibility, sentiment, and competitive presence, with a specific focus on **Atomberg vs competitors**.

---

## **Problem Statement**

Brands compete not just on product quality, but on **visibility during discovery and consideration**.
This project answers the question:

> *How visible is Atomberg compared to competitors when users search for generic keywords like “smart fan”?*

---

## **Approach Overview**

The pipeline:

1. Searches Google for a given keyword
2. Extracts top organic results
3. Scrapes page content
4. Detects brand mentions
5. Applies sentiment analysis
6. Computes a weighted Share of Voice score

The solution is **modular, explainable, and extensible** to other keywords or platforms.

---



## **How It Works**

### 1. Keyword Search

Uses SerpAPI to fetch the **top N organic Google results** for a given keyword (default: 10).

### 2. Source Classification

Each result is classified into:

* Brand Site
* Marketplace
* Editorial / Informational

This avoids marketplaces or brand SEO pages skewing results unfairly.

### 3. Brand Mention Detection

* Tracks mentions for Atomberg and competitors
* Uses case-insensitive, word-boundary matching

### 4. Sentiment Analysis

* Uses VADER to label mentions as positive, neutral, or negative
* Positive mentions contribute more to SoV

### 5. Share of Voice Calculation

SoV is computed using:

* Search rank weighting
* Source type weighting
* Sentiment weighting

Final output is a normalized distribution across brands.

---

## **Interpretation**

* Atomberg performs strongly on **owned media**
* Under-represented on **editorial and comparison-driven content**
* Indicates a **top-of-funnel visibility gap**, not a product weakness

---

## **Setup Instructions**

### 1. Clone Repository

```bash
git clone <repo-url>
cd <repo-name>
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set SerpAPI Key

```bash
export SERP_API_KEY="your_api_key"
```

### 5. Run the Pipeline

```bash
python main.py
```

---

## **Extending the Project**

* Add more keywords for multi-keyword SoV analysis
* Integrate YouTube / Instagram search results
* Add engagement-based weighting
* Store historical SoV trends for time-series analysis

---

## **Limitations**

* Google-only analysis (social platforms not yet included)
* Engagement metrics inferred, not directly measured
* Sentiment analysis is rule-based, not LLM-based

---

## **Why This Approach**

* Transparent and auditable
* Avoids SEO verbosity bias
* Aligns with real user discovery behavior
* Easy to scale and productionize

