"""
Auto-generated skill: skill_7_0_bfed0e
Level: 7
Generated: 2026-03-28T22:37:01.518384Z
Description: Auto-generated skill skill_7_0_bfed0e (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_bfed0e", "level": 7, "desc": "Auto-generated skill skill_7_0_bfed0e (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
