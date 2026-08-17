"""
Auto-generated skill: skill_7_1_421c1c
Level: 8
Generated: 2026-08-17T22:30:15.579496Z
Description: Auto-generated skill skill_7_1_421c1c (Level: 8) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_1_421c1c", "level": 8, "desc": "Auto-generated skill skill_7_1_421c1c (Level: 8) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 8) * 8)
