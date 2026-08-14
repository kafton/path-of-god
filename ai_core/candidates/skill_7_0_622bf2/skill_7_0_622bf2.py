"""
Auto-generated skill: skill_7_0_622bf2
Level: 7
Generated: 2026-08-14T22:30:01.859145Z
Description: Auto-generated skill skill_7_0_622bf2 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_622bf2", "level": 7, "desc": "Auto-generated skill skill_7_0_622bf2 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
