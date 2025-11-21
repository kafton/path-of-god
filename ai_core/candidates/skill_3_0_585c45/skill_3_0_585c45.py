"""
Auto-generated skill: skill_3_0_585c45
Level: 3
Generated: 2025-11-21T14:15:00.962688Z
Description: Auto-generated skill skill_3_0_585c45 (Level: 3) - optimizer heuristic
"""

def info():
    return {"name": "skill_3_0_585c45", "level": 3, "desc": "Auto-generated skill skill_3_0_585c45 (Level: 3) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 3) * 3)
