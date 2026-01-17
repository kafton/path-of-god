"""
Auto-generated skill: skill_7_0_586b46
Level: 7
Generated: 2026-01-17T22:26:31.620093Z
Description: Auto-generated skill skill_7_0_586b46 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_586b46", "level": 7, "desc": "Auto-generated skill skill_7_0_586b46 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
