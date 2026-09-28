"""
Auto-generated skill: skill_7_0_413686
Level: 7
Generated: 2026-09-28T00:28:16.746019Z
Description: Auto-generated skill skill_7_0_413686 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_413686", "level": 7, "desc": "Auto-generated skill skill_7_0_413686 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
