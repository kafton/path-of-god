"""
Auto-generated skill: skill_7_0_5c444f
Level: 7
Generated: 2025-12-24T22:26:43.417223Z
Description: Auto-generated skill skill_7_0_5c444f (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_5c444f", "level": 7, "desc": "Auto-generated skill skill_7_0_5c444f (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
