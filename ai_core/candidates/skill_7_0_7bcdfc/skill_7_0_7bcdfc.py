"""
Auto-generated skill: skill_7_0_7bcdfc
Level: 7
Generated: 2026-05-18T23:11:03.516071Z
Description: Auto-generated skill skill_7_0_7bcdfc (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_7bcdfc", "level": 7, "desc": "Auto-generated skill skill_7_0_7bcdfc (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
