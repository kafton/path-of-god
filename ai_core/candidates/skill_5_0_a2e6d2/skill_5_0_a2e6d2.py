"""
Auto-generated skill: skill_5_0_a2e6d2
Level: 5
Generated: 2025-11-22T06:30:32.666589Z
Description: Auto-generated skill skill_5_0_a2e6d2 (Level: 5) - optimizer heuristic
"""

def info():
    return {"name": "skill_5_0_a2e6d2", "level": 5, "desc": "Auto-generated skill skill_5_0_a2e6d2 (Level: 5) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 5) * 5)
