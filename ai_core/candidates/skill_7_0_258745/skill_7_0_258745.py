"""
Auto-generated skill: skill_7_0_258745
Level: 7
Generated: 2026-08-01T22:59:15.790302Z
Description: Auto-generated skill skill_7_0_258745 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_258745", "level": 7, "desc": "Auto-generated skill skill_7_0_258745 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
