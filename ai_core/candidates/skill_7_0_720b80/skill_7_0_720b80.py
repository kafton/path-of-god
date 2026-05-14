"""
Auto-generated skill: skill_7_0_720b80
Level: 7
Generated: 2026-05-14T23:03:17.044179Z
Description: Auto-generated skill skill_7_0_720b80 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_720b80", "level": 7, "desc": "Auto-generated skill skill_7_0_720b80 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
