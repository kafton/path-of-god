#!/usr/bin/env python3
"""
Free Search Module (DuckDuckGo + Wikipedia + Safe Scraper)
No API keys required.
"""

import requests
import re

# ---------------------------------------------------------
# DuckDuckGo Instant Answer SEARCH (free)
# ---------------------------------------------------------
def ddg_search(query):
    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json",
        "no_html": 1,
        "skip_disambig": 1,
    }

    try:
        r = requests.get(url, params=params, timeout=5)
        data = r.json()
    except Exception as e:
        return {"error": f"DDG request failed: {e}"}

    abstract = data.get("Abstract")
    heading = data.get("Heading")
    answer = data.get("Answer")

    result = {
        "query": query,
        "heading": heading or "",
        "abstract": abstract or "",
        "answer": answer or "",
    }

    return result


# ---------------------------------------------------------
# Wikipedia Summary Search
# ---------------------------------------------------------
def wiki_search(query):
    search_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '%20')}"

    try:
        r = requests.get(search_url, timeout=5)
        data = r.json()
    except Exception as e:
        return {"error": f"Wikipedia request failed: {e}"}

    if "extract" not in data:
        return {"error": "No summary available"}

    return {
        "title": data.get("title", ""),
        "description": data.get("description", ""),
        "extract": data.get("extract", "")
    }


# ---------------------------------------------------------
# SAFE SCRAPER (free)
# ---------------------------------------------------------
BLOCKED_DOMAINS = ["facebook.com", "x.com", "twitter.com", "tiktok.com"]

def safe_scrape(url):
    for bad in BLOCKED_DOMAINS:
        if bad in url.lower():
            return {"error": "Blocked domain for safety"}

    try:
        r = requests.get(url, timeout=5)
        text = r.text
    except Exception as e:
        return {"error": f"Scrape failed: {e}"}

    clean = re.sub("<.*?>", " ", text)
    clean = re.sub(r"\s+", " ", clean)

    return {"url": url, "content": clean[:1500]}
