"""
Auto-generated skill: skill_7_0_15af71
Level: 7
Generated: 2026-09-01T01:10:18.479977Z
Description: Auto-generated skill skill_7_0_15af71 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_15af71", "level": 7, "desc": "Auto-generated skill skill_7_0_15af71 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
