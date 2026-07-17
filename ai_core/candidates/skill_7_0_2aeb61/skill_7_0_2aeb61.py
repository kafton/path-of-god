"""
Auto-generated skill: skill_7_0_2aeb61
Level: 7
Generated: 2026-07-17T22:54:46.591468Z
Description: Auto-generated skill skill_7_0_2aeb61 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_2aeb61", "level": 7, "desc": "Auto-generated skill skill_7_0_2aeb61 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
