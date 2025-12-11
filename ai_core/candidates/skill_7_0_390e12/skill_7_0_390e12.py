"""
Auto-generated skill: skill_7_0_390e12
Level: 7
Generated: 2025-12-11T22:27:19.482896Z
Description: Auto-generated skill skill_7_0_390e12 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_390e12", "level": 7, "desc": "Auto-generated skill skill_7_0_390e12 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
