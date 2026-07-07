"""
Auto-generated skill: skill_7_0_3fb14e
Level: 7
Generated: 2026-07-07T23:07:30.467943Z
Description: Auto-generated skill skill_7_0_3fb14e (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_3fb14e", "level": 7, "desc": "Auto-generated skill skill_7_0_3fb14e (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
