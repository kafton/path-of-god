"""
Auto-generated skill: skill_7_0_41af66
Level: 7
Generated: 2026-10-15T00:23:11.388049Z
Description: Auto-generated skill skill_7_0_41af66 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_41af66", "level": 7, "desc": "Auto-generated skill skill_7_0_41af66 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
