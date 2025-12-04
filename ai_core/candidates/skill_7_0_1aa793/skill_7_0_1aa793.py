"""
Auto-generated skill: skill_7_0_1aa793
Level: 7
Generated: 2025-12-04T22:24:38.006474Z
Description: Auto-generated skill skill_7_0_1aa793 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_1aa793", "level": 7, "desc": "Auto-generated skill skill_7_0_1aa793 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
