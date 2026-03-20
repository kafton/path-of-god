"""
Auto-generated skill: skill_7_1_2587c3
Level: 8
Generated: 2026-03-20T22:36:35.910591Z
Description: Auto-generated skill skill_7_1_2587c3 (Level: 8) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_1_2587c3", "level": 8, "desc": "Auto-generated skill skill_7_1_2587c3 (Level: 8) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 8) * 8)
