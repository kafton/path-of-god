"""
Auto-generated skill: skill_7_0_f96e16
Level: 7
Generated: 2026-10-08T01:42:58.811639Z
Description: Auto-generated skill skill_7_0_f96e16 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_f96e16", "level": 7, "desc": "Auto-generated skill skill_7_0_f96e16 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
