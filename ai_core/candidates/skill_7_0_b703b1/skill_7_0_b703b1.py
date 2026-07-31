"""
Auto-generated skill: skill_7_0_b703b1
Level: 7
Generated: 2026-07-31T23:08:56.415102Z
Description: Auto-generated skill skill_7_0_b703b1 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_b703b1", "level": 7, "desc": "Auto-generated skill skill_7_0_b703b1 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
