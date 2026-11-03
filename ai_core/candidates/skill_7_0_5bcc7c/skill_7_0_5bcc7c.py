"""
Auto-generated skill: skill_7_0_5bcc7c
Level: 7
Generated: 2026-11-03T03:24:16.090458Z
Description: Auto-generated skill skill_7_0_5bcc7c (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_5bcc7c", "level": 7, "desc": "Auto-generated skill skill_7_0_5bcc7c (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
