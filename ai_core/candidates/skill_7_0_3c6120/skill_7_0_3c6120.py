"""
Auto-generated skill: skill_7_0_3c6120
Level: 7
Generated: 2026-06-02T23:53:03.620692Z
Description: Auto-generated skill skill_7_0_3c6120 (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_3c6120", "level": 7, "desc": "Auto-generated skill skill_7_0_3c6120 (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
