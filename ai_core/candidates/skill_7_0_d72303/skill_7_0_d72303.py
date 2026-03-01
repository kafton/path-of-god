"""
Auto-generated skill: skill_7_0_d72303
Level: 7
Generated: 2026-03-01T22:32:01.899271Z
Description: Auto-generated skill skill_7_0_d72303 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_d72303", "level": 7, "desc": "Auto-generated skill skill_7_0_d72303 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
