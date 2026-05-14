"""
Auto-generated skill: skill_7_1_a5461c
Level: 8
Generated: 2026-05-14T23:03:17.665967Z
Description: Auto-generated skill skill_7_1_a5461c (Level: 8) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_1_a5461c", "level": 8, "desc": "Auto-generated skill skill_7_1_a5461c (Level: 8) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 8) * 8)
