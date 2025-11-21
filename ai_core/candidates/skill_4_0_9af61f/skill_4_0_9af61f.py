"""
Auto-generated skill: skill_4_0_9af61f
Level: 4
Generated: 2025-11-21T22:25:54.522677Z
Description: Auto-generated skill skill_4_0_9af61f (Level: 4) - optimizer heuristic
"""

def info():
    return {"name": "skill_4_0_9af61f", "level": 4, "desc": "Auto-generated skill skill_4_0_9af61f (Level: 4) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 4) * 4)
