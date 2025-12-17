"""
Auto-generated skill: skill_7_0_f730bb
Level: 7
Generated: 2025-12-17T22:27:06.427387Z
Description: Auto-generated skill skill_7_0_f730bb (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_f730bb", "level": 7, "desc": "Auto-generated skill skill_7_0_f730bb (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
