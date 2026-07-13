"""
Auto-generated skill: skill_7_0_297705
Level: 7
Generated: 2026-07-13T23:01:08.744770Z
Description: Auto-generated skill skill_7_0_297705 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_297705", "level": 7, "desc": "Auto-generated skill skill_7_0_297705 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
