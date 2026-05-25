"""
Auto-generated skill: skill_7_0_2ec745
Level: 7
Generated: 2026-05-25T23:12:55.803063Z
Description: Auto-generated skill skill_7_0_2ec745 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_2ec745", "level": 7, "desc": "Auto-generated skill skill_7_0_2ec745 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
