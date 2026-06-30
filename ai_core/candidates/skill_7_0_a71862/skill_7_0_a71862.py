"""
Auto-generated skill: skill_7_0_a71862
Level: 7
Generated: 2026-06-30T23:18:27.178951Z
Description: Auto-generated skill skill_7_0_a71862 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_a71862", "level": 7, "desc": "Auto-generated skill skill_7_0_a71862 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
