"""
Auto-generated skill: skill_7_0_71e591
Level: 7
Generated: 2026-05-28T23:22:36.723415Z
Description: Auto-generated skill skill_7_0_71e591 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_71e591", "level": 7, "desc": "Auto-generated skill skill_7_0_71e591 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
