"""
Auto-generated skill: skill_7_0_8e20ba
Level: 7
Generated: 2026-04-28T23:01:00.845369Z
Description: Auto-generated skill skill_7_0_8e20ba (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_8e20ba", "level": 7, "desc": "Auto-generated skill skill_7_0_8e20ba (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
