"""
Auto-generated skill: skill_7_0_a2f390
Level: 7
Generated: 2026-01-19T22:28:44.584185Z
Description: Auto-generated skill skill_7_0_a2f390 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_a2f390", "level": 7, "desc": "Auto-generated skill skill_7_0_a2f390 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
