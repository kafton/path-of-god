"""
Auto-generated skill: skill_4
Level: 4
Generated: 2025-11-21T22:11:28.913478Z
"""

def info():
    return {
        "name": "skill_4",
        "level": 4,
        "desc": "Auto-generated skill that computes an integer score."
    }

def run(input_value: int) -> int:
    """
    Simple deterministic function that returns an integer score.
    This is intentionally simple and testable.
    """
    # skill behavior scales with level
    return max(0, (input_value + 4) * 4)
