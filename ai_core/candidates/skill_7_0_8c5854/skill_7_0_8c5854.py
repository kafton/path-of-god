"""
Auto-generated skill: skill_7_0_8c5854
Level: 7
Generated: 2025-12-30T22:26:32.725358Z
Description: Auto-generated skill skill_7_0_8c5854 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_8c5854", "level": 7, "desc": "Auto-generated skill skill_7_0_8c5854 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
