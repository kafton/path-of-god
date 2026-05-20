"""
Auto-generated skill: skill_7_0_6c7b13
Level: 7
Generated: 2026-05-20T23:18:43.090372Z
Description: Auto-generated skill skill_7_0_6c7b13 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_6c7b13", "level": 7, "desc": "Auto-generated skill skill_7_0_6c7b13 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
