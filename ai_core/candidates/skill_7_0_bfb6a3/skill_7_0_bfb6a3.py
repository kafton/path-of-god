"""
Auto-generated skill: skill_7_0_bfb6a3
Level: 7
Generated: 2026-08-07T01:30:53.640941Z
Description: Auto-generated skill skill_7_0_bfb6a3 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_bfb6a3", "level": 7, "desc": "Auto-generated skill skill_7_0_bfb6a3 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
