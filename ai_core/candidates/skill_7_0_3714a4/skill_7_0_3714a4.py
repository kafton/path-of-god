"""
Auto-generated skill: skill_7_0_3714a4
Level: 7
Generated: 2026-09-23T00:13:47.296090Z
Description: Auto-generated skill skill_7_0_3714a4 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_3714a4", "level": 7, "desc": "Auto-generated skill skill_7_0_3714a4 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
