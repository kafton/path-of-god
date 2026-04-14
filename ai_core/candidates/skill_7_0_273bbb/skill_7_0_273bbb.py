"""
Auto-generated skill: skill_7_0_273bbb
Level: 7
Generated: 2026-04-14T22:52:51.656934Z
Description: Auto-generated skill skill_7_0_273bbb (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_273bbb", "level": 7, "desc": "Auto-generated skill skill_7_0_273bbb (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
