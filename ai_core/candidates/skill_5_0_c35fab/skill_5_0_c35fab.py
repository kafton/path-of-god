"""
Auto-generated skill: skill_5_0_c35fab
Level: 5
Generated: 2025-11-22T07:05:25.475422Z
Description: Auto-generated skill skill_5_0_c35fab (Level: 5) - optimizer heuristic
"""

def info():
    return {"name": "skill_5_0_c35fab", "level": 5, "desc": "Auto-generated skill skill_5_0_c35fab (Level: 5) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 5) * 5)
