"""
Auto-generated skill: skill_7_0_4e271f
Level: 7
Generated: 2026-03-21T22:33:11.572602Z
Description: Auto-generated skill skill_7_0_4e271f (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_4e271f", "level": 7, "desc": "Auto-generated skill skill_7_0_4e271f (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
