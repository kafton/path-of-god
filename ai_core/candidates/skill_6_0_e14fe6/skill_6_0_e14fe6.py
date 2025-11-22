"""
Auto-generated skill: skill_6_0_e14fe6
Level: 6
Generated: 2025-11-22T11:01:28.178783Z
Description: Auto-generated skill skill_6_0_e14fe6 (Level: 6) - optimizer heuristic
"""

def info():
    return {"name": "skill_6_0_e14fe6", "level": 6, "desc": "Auto-generated skill skill_6_0_e14fe6 (Level: 6) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 6) * 6)
