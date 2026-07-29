"""
Auto-generated skill: skill_7_0_5770b6
Level: 7
Generated: 2026-07-29T23:03:02.445910Z
Description: Auto-generated skill skill_7_0_5770b6 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_5770b6", "level": 7, "desc": "Auto-generated skill skill_7_0_5770b6 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
