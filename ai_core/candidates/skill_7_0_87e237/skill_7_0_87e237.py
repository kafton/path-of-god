"""
Auto-generated skill: skill_7_0_87e237
Level: 7
Generated: 2026-07-18T22:56:04.358021Z
Description: Auto-generated skill skill_7_0_87e237 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_87e237", "level": 7, "desc": "Auto-generated skill skill_7_0_87e237 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
