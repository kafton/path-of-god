"""
Auto-generated skill: skill_7_0_cf37d0
Level: 7
Generated: 2026-05-07T23:03:51.839288Z
Description: Auto-generated skill skill_7_0_cf37d0 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_cf37d0", "level": 7, "desc": "Auto-generated skill skill_7_0_cf37d0 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
