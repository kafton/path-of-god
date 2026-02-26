"""
Auto-generated skill: skill_7_0_e12272
Level: 7
Generated: 2026-02-26T22:40:53.794271Z
Description: Auto-generated skill skill_7_0_e12272 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_e12272", "level": 7, "desc": "Auto-generated skill skill_7_0_e12272 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
