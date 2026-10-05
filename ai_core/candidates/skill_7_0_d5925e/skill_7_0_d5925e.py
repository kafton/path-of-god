"""
Auto-generated skill: skill_7_0_d5925e
Level: 7
Generated: 2026-10-05T00:39:24.757811Z
Description: Auto-generated skill skill_7_0_d5925e (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_d5925e", "level": 7, "desc": "Auto-generated skill skill_7_0_d5925e (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
