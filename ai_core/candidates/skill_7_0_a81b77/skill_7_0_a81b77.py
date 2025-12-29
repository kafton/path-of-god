"""
Auto-generated skill: skill_7_0_a81b77
Level: 7
Generated: 2025-12-29T22:26:51.285183Z
Description: Auto-generated skill skill_7_0_a81b77 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_a81b77", "level": 7, "desc": "Auto-generated skill skill_7_0_a81b77 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
