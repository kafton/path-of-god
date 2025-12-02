"""
Auto-generated skill: skill_7_0_e5870e
Level: 7
Generated: 2025-12-02T22:23:23.285030Z
Description: Auto-generated skill skill_7_0_e5870e (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_e5870e", "level": 7, "desc": "Auto-generated skill skill_7_0_e5870e (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
