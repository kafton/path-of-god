"""
Auto-generated skill: skill_3_2_139854
Level: 5
Generated: 2025-11-21T14:15:01.946357Z
Description: Auto-generated skill skill_3_2_139854 (Level: 5) - optimizer heuristic
"""

def info():
    return {"name": "skill_3_2_139854", "level": 5, "desc": "Auto-generated skill skill_3_2_139854 (Level: 5) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 5) * 5)
