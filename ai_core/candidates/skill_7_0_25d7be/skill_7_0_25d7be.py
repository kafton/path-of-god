"""
Auto-generated skill: skill_7_0_25d7be
Level: 7
Generated: 2026-03-31T22:41:13.053114Z
Description: Auto-generated skill skill_7_0_25d7be (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_25d7be", "level": 7, "desc": "Auto-generated skill skill_7_0_25d7be (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
