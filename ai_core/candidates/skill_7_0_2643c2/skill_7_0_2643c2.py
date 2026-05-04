"""
Auto-generated skill: skill_7_0_2643c2
Level: 7
Generated: 2026-05-04T23:00:44.584683Z
Description: Auto-generated skill skill_7_0_2643c2 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_2643c2", "level": 7, "desc": "Auto-generated skill skill_7_0_2643c2 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
