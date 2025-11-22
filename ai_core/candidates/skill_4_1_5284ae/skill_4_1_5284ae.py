"""
Auto-generated skill: skill_4_1_5284ae
Level: 5
Generated: 2025-11-21T22:25:54.991894Z
Description: Auto-generated skill skill_4_1_5284ae (Level: 5) - optimizer heuristic
"""

def info():
    return {"name": "skill_4_1_5284ae", "level": 5, "desc": "Auto-generated skill skill_4_1_5284ae (Level: 5) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 5) * 5)
