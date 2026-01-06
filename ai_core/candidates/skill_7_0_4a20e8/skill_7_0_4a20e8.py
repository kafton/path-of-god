"""
Auto-generated skill: skill_7_0_4a20e8
Level: 7
Generated: 2026-01-06T22:28:57.888496Z
Description: Auto-generated skill skill_7_0_4a20e8 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_4a20e8", "level": 7, "desc": "Auto-generated skill skill_7_0_4a20e8 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
