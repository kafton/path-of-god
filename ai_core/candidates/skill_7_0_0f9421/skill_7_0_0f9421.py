"""
Auto-generated skill: skill_7_0_0f9421
Level: 7
Generated: 2026-01-02T22:27:44.781510Z
Description: Auto-generated skill skill_7_0_0f9421 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_0f9421", "level": 7, "desc": "Auto-generated skill skill_7_0_0f9421 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
