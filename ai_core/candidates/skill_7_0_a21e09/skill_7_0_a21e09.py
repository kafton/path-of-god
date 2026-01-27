"""
Auto-generated skill: skill_7_0_a21e09
Level: 7
Generated: 2026-01-27T22:29:20.715036Z
Description: Auto-generated skill skill_7_0_a21e09 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_a21e09", "level": 7, "desc": "Auto-generated skill skill_7_0_a21e09 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
