"""
Auto-generated skill: skill_7_0_5075bb
Level: 7
Generated: 2026-03-03T22:37:13.913324Z
Description: Auto-generated skill skill_7_0_5075bb (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_5075bb", "level": 7, "desc": "Auto-generated skill skill_7_0_5075bb (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
