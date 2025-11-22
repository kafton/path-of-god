"""
Auto-generated skill: skill_6_1_fe408e
Level: 7
Generated: 2025-11-22T11:01:28.723883Z
Description: Auto-generated skill skill_6_1_fe408e (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_6_1_fe408e", "level": 7, "desc": "Auto-generated skill skill_6_1_fe408e (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
