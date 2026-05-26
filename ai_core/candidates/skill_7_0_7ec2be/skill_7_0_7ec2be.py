"""
Auto-generated skill: skill_7_0_7ec2be
Level: 7
Generated: 2026-05-26T23:14:50.422037Z
Description: Auto-generated skill skill_7_0_7ec2be (Level: 7) - optimizer heuristic
"""

def info():
    return {"name": "skill_7_0_7ec2be", "level": 7, "desc": "Auto-generated skill skill_7_0_7ec2be (Level: 7) - optimizer heuristic"}

def run(x: int) -> int:
    # deterministic scoring function
    return max(0, (x + 7) * 7)
