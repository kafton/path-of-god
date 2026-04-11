"""
Auto-generated skill: skill_7_1_096771
Level: 8
Generated: 2026-04-11T22:39:42.100185Z
Description: Auto-generated skill skill_7_1_096771 (Level: 8) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_1_096771", "level": 8, "desc": "Auto-generated skill skill_7_1_096771 (Level: 8) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 8) * 8)
