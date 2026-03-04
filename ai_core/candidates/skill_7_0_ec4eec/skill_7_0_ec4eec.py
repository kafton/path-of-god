"""
Auto-generated skill: skill_7_0_ec4eec
Level: 7
Generated: 2026-03-04T22:38:57.520758Z
Description: Auto-generated skill skill_7_0_ec4eec (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_ec4eec", "level": 7, "desc": "Auto-generated skill skill_7_0_ec4eec (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
