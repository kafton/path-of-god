"""
Auto-generated skill: skill_7_0_af2809
Level: 7
Generated: 2026-02-08T22:35:38.001058Z
Description: Auto-generated skill skill_7_0_af2809 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_af2809", "level": 7, "desc": "Auto-generated skill skill_7_0_af2809 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
