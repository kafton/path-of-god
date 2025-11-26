"""
Auto-generated skill: skill_7_0_20b7d6
Level: 7
Generated: 2025-11-26T22:25:39.931036Z
Description: Auto-generated skill skill_7_0_20b7d6 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_20b7d6", "level": 7, "desc": "Auto-generated skill skill_7_0_20b7d6 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
