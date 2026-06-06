"""
Auto-generated skill: skill_7_0_7a5896
Level: 7
Generated: 2026-06-06T23:09:50.011442Z
Description: Auto-generated skill skill_7_0_7a5896 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_7a5896", "level": 7, "desc": "Auto-generated skill skill_7_0_7a5896 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
