"""
Auto-generated skill: skill_7_0_ae891c
Level: 7
Generated: 2026-09-19T00:05:24.798096Z
Description: Auto-generated skill skill_7_0_ae891c (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_ae891c", "level": 7, "desc": "Auto-generated skill skill_7_0_ae891c (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
