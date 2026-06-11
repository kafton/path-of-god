"""
Auto-generated skill: skill_7_0_014760
Level: 7
Generated: 2026-06-11T23:42:44.167493Z
Description: Auto-generated skill skill_7_0_014760 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_014760", "level": 7, "desc": "Auto-generated skill skill_7_0_014760 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
