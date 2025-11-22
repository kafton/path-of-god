"""
Auto-generated skill: skill_5_2_a6f495
Level: 7
Generated: 2025-11-22T06:30:33.517958Z
Description: Auto-generated skill skill_5_2_a6f495 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_5_2_a6f495", "level": 7, "desc": "Auto-generated skill skill_5_2_a6f495 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
