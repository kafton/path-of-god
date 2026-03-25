"""
Auto-generated skill: skill_7_0_b3a371
Level: 7
Generated: 2026-03-25T22:45:51.911275Z
Description: Auto-generated skill skill_7_0_b3a371 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_b3a371", "level": 7, "desc": "Auto-generated skill skill_7_0_b3a371 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
