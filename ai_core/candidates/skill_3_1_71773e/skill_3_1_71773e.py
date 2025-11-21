"""
Auto-generated skill: skill_3_1_71773e
Level: 4
Generated: 2025-11-21T14:15:01.636132Z
Description: Auto-generated skill skill_3_1_71773e (Level: 4) - optimizer heuristic
"""

def info():
    return {"name": "skill_3_1_71773e", "level": 4, "desc": "Auto-generated skill skill_3_1_71773e (Level: 4) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 4) * 4)
