"""
Auto-generated skill: skill_7_0_5d1236
Level: 7
Generated: 2025-12-23T22:26:39.432289Z
Description: Auto-generated skill skill_7_0_5d1236 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_5d1236", "level": 7, "desc": "Auto-generated skill skill_7_0_5d1236 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
