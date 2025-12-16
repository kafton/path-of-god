"""
Auto-generated skill: skill_7_0_5f94a7
Level: 7
Generated: 2025-12-16T22:25:35.591019Z
Description: Auto-generated skill skill_7_0_5f94a7 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_5f94a7", "level": 7, "desc": "Auto-generated skill skill_7_0_5f94a7 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
