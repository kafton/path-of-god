"""
Auto-generated skill: skill_7_0_aaf5b6
Level: 7
Generated: 2026-05-10T22:55:36.351041Z
Description: Auto-generated skill skill_7_0_aaf5b6 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_aaf5b6", "level": 7, "desc": "Auto-generated skill skill_7_0_aaf5b6 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
