"""
Auto-generated skill: skill_7_0_d0129f
Level: 7
Generated: 2025-12-19T22:26:41.285377Z
Description: Auto-generated skill skill_7_0_d0129f (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_d0129f", "level": 7, "desc": "Auto-generated skill skill_7_0_d0129f (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
