"""
Auto-generated skill: skill_7_0_a964c1
Level: 7
Generated: 2026-01-05T22:28:30.600164Z
Description: Auto-generated skill skill_7_0_a964c1 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_a964c1", "level": 7, "desc": "Auto-generated skill skill_7_0_a964c1 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
