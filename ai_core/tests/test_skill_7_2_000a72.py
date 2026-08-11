"""
Auto-test for skill_7_2_000a72
"""

from ai_core.skills import skill_7_2_000a72 as skill

def test_skill_7_2_000a72_basic():
    assert skill.run(0) == ((0 + 9) * 9)
    assert isinstance(skill.run(1), int)
