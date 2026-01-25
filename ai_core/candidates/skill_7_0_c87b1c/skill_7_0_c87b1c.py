"""
Auto-generated skill: skill_7_0_c87b1c
Level: 7
Generated: 2026-01-25T22:27:41.991928Z
Description: Auto-generated skill skill_7_0_c87b1c (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_c87b1c", "level": 7, "desc": "Auto-generated skill skill_7_0_c87b1c (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
