"""
Auto-generated skill: skill_7_0_ad680f
Level: 7
Generated: 2026-07-09T23:18:11.385342Z
Description: Auto-generated skill skill_7_0_ad680f (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_ad680f", "level": 7, "desc": "Auto-generated skill skill_7_0_ad680f (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
