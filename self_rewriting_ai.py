#!/usr/bin/env python3
"""
Self-rewriting AI with integrated free search (inside rewrite block).
- Memory persisted to ai_memory.json
- Rewrites only the marked block between START_TAG and END_TAG
- The rewrite block contains search functions (DuckDuckGo, Wikipedia, safe_scrape)
  and the ai_decision_engine, so the AI can evolve search behavior.
- Atomic writes and basic safety checks included.
"""

import json
import os
import re
from datetime import datetime

AI_FILE = os.path.abspath(__file__)
MEMORY_FILE = "ai_memory.json"

# -------------------------------------------------------------------
# MEMORY SYSTEM
# -------------------------------------------------------------------
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"knowledge": 1, "reward": 0, "history": []}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4)

memory = load_memory()

# -------------------------------------------------------------------
# AI REWARD AND IMPROVEMENT LOGIC
# -------------------------------------------------------------------
def reward_ai(amount=1):
    memory["reward"] = memory.get("reward", 0) + amount
    memory["knowledge"] = memory.get("knowledge", 0) + amount
    memory.setdefault("history", []).append({
        "time": datetime.utcnow().isoformat() + "Z",
        "event": f"AI improved knowledge by {amount}"
    })
    save_memory(memory)

# -------------------------------------------------------------------
# SELF-REFLECTION SYSTEM
# -------------------------------------------------------------------
def reflect(memory_obj):
    k = memory_obj.get("knowledge", 0)
    r = memory_obj.get("reward", 0)
    reflection = (
        f"The AI currently has:\n"
        f"- Knowledge Level: {k}\n"
        f"- Reward Score: {r}\n\n"
        "Reflection:\n"
        "I will focus on improving internal functions inside allowed blocks.\n"
    )
    memory_obj.setdefault("history", []).append(
        {"time": datetime.utcnow().isoformat() + "Z", "reflection": reflection}
    )
    save_memory(memory_obj)
    return reflection

# -------------------------------------------------------------------
# SAFE SELF-REWRITING ENGINE
# -------------------------------------------------------------------
START_TAG = "# === AI_REWRITE_START ==="
END_TAG   = "# === AI_REWRITE_END ==="

def generate_improved_code(old_code_block, memory_obj):
    """
    Generate an improved code block. This function returns a string which
    will replace the current rewrite region. The generated block includes
    search utilities and the ai_decision_engine; here we keep it simple and
    use memory to set level/reward values.
    """
    lvl = int(memory_obj.get("knowledge", 1))
    reward = int(memory_obj.get("reward", 0))

    # This template contains both search functions and the decision engine.
    # The AI will be allowed to mutate this entire block in future runs.
    new_code = f'''
# === BEGIN AUTO-GENERATED SEARCH + DECISION BLOCK ===

# Free search: DuckDuckGo Instant Answer (no key), Wikipedia summary, safe_scrape
import requests
import re
from urllib.parse import quote, urlparse

def ddg_search(query, timeout=6):
    try:
        resp = requests.get("https://api.duckduckgo.com/",
                            params={{"q": query, "format": "json", "no_html": 1, "no_redirect": 1}},
                            timeout=timeout,
                            headers={{"User-Agent":"ai-sandbox/1.0"}})
        resp.raise_for_status()
        data = resp.json()
        return {{
            "query": query,
            "heading": data.get("Heading",""),
            "abstract": data.get("Abstract",""),
            "answer": data.get("Answer","")
        }}
    except Exception as e:
        return {{"error": str(e)}}

def wiki_search(query, timeout=6):
    try:
        safe_q = quote(query.replace(" ", "_"))
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{{safe_q}}"
        resp = requests.get(url, timeout=timeout, headers={{"User-Agent":"ai-sandbox/1.0"}})
        resp.raise_for_status()
        data = resp.json()
        if "extract" in data:
            return {{"title": data.get("title",""), "extract": data.get("extract","")}}
        return {{"error":"no summary"}}
    except Exception as e:
        return {{"error": str(e)}}

# Very small safe_scrape with a blocklist and truncation
BLOCKLIST = {{"google.com","www.google.com","facebook.com","twitter.com","instagram.com"}}
def safe_scrape(url, timeout=6, max_chars=1500):
    try:
        parsed = urlparse(url)
        host = (parsed.hostname or "").lower()
        if any(b in host for b in BLOCKLIST):
            return {{"error":"domain blocked"}}
        resp = requests.get(url, timeout=timeout, headers={{"User-Agent":"ai-sandbox/1.0"}})
        resp.raise_for_status()
        text = re.sub(r"<.*?>", " ", resp.text)
        text = re.sub(r"\\s+", " ", text)
        return {{"text": text[:max_chars]}}
    except Exception as e:
        return {{"error": str(e)}}

# AI decision engine (auto-generated)
def ai_decision_engine():
    knowledge = {lvl}
    reward = {reward}
    # Example behavior: prefer Wikipedia summary if available, else DuckDuckGo answer
    def query_and_pick(q):
        w = wiki_search(q)
        if isinstance(w, dict) and w.get("extract"):
            return {{"source":"wikipedia","summary": w.get("extract")}}
        dd = ddg_search(q)
        if isinstance(dd, dict) and dd.get("abstract"):
            return {{"source":"duckduckgo","summary": dd.get("abstract")}}
        return {{"source":"none","summary": ""}}

    # Decision value is deterministic for testing and evolution
    decision_value = (knowledge * 10) + reward
    return {{
        "knowledge": knowledge,
        "reward": reward,
        "decision_value": decision_value,
        "query_and_pick": query_and_pick  # note: functions can't be serialized; used at runtime only
    }}

# === END AUTO-GENERATED SEARCH + DECISION BLOCK ===
'''
    return new_code

def rewrite_self():
    # Read own file
    with open(AI_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Locate rewrite block
    pattern = re.compile(re.escape(START_TAG) + r"(.*?)" + re.escape(END_TAG), re.DOTALL)
    m = pattern.search(content)
    if not m:
        print("❌ Rewrite markers not found. No changes made.")
        return False

    old_block = m.group(1)
    new_block = "\n" + generate_improved_code(old_block, memory) + "\n"
    updated = content[:m.start(1)] + new_block + content[m.end(1):]

    # Safety check: tags must remain
    if START_TAG not in updated or END_TAG not in updated:
        print("❌ Safety check failed: tags missing after update.")
        return False

    # Atomic write
    tmp = AI_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(updated)
    os.replace(tmp, AI_FILE)

    print("✅ AI successfully rewrote its own code.")
    return True

# -------------------------------------------------------------------
# MAIN EXECUTION
# -------------------------------------------------------------------
def main():
    print("=== AI SELF EVOLUTION START ===")
    print(f"Current knowledge: {memory.get('knowledge')} | reward: {memory.get('reward')}")
    reflect(memory)
    reward_ai(1)
    ok = rewrite_self()
    if ok:
        memory.setdefault("history", []).append({
            "time": datetime.utcnow().isoformat() + "Z",
            "event": "rewrite_success"
        })
        save_memory(memory)
    print("AI knowledge increased to:", memory.get("knowledge"))
    print("=== AI SELF EVOLUTION END ===")

if __name__ == "__main__":
    main()

# -------------------------------------------------------------------
# REWRITE MARKERS (the AI can modify everything between these)
# -------------------------------------------------------------------
# === AI_REWRITE_START ===
# (initial block — will be replaced by the first rewrite)
def ai_decision_engine():
    # initial placeholder behavior before first rewrite
    return {"knowledge": 1, "reward": 0, "decision_value": 0}
# === AI_REWRITE_END ===
