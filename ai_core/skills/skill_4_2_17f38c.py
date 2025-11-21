"""
Auto-generated skill: skill_4_2_17f38c
Level: 6
Generated: 2025-11-21T22:25:55.321226Z
Description: Auto-generated skill skill_4_2_17f38c (Level: 6) - optimizer heuristic
"""

def info():
    return {"name": "skill_4_2_17f38c", "level": 6, "desc": "Auto-generated skill skill_4_2_17f38c (Level: 6) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 6) * 6)
