"""
Auto-generated skill: skill_7_0_6482a0
Level: 7
Generated: 2026-02-27T22:31:33.118003Z
Description: Auto-generated skill skill_7_0_6482a0 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_6482a0", "level": 7, "desc": "Auto-generated skill skill_7_0_6482a0 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
