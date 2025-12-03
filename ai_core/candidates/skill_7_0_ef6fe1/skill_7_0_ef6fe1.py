"""
Auto-generated skill: skill_7_0_ef6fe1
Level: 7
Generated: 2025-12-03T22:27:05.460094Z
Description: Auto-generated skill skill_7_0_ef6fe1 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_ef6fe1", "level": 7, "desc": "Auto-generated skill skill_7_0_ef6fe1 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
