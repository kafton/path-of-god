"""
Auto-generated skill: skill_7_0_c62ce6
Level: 7
Generated: 2026-06-27T23:09:22.181496Z
Description: Auto-generated skill skill_7_0_c62ce6 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_c62ce6", "level": 7, "desc": "Auto-generated skill skill_7_0_c62ce6 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
