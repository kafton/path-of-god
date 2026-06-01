"""
Auto-generated skill: skill_7_0_5d0d81
Level: 7
Generated: 2026-06-01T23:39:16.861290Z
Description: Auto-generated skill skill_7_0_5d0d81 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_5d0d81", "level": 7, "desc": "Auto-generated skill skill_7_0_5d0d81 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
