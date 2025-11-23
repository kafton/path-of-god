"""
Auto-test for skill_6_2_4e8432
"""

from ai_core.skills import skill_6_2_4e8432 as skill

def test_skill_6_2_4e8432_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
