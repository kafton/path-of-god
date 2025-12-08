"""
Auto-generated skill: skill_7_0_5986e3
Level: 7
Generated: 2025-12-08T22:26:18.963133Z
Description: Auto-generated skill skill_7_0_5986e3 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_5986e3", "level": 7, "desc": "Auto-generated skill skill_7_0_5986e3 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
