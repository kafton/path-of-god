"""
Auto-generated skill: skill_7_0_7207ca
Level: 7
Generated: 2026-09-29T01:43:07.771851Z
Description: Auto-generated skill skill_7_0_7207ca (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_7207ca", "level": 7, "desc": "Auto-generated skill skill_7_0_7207ca (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
