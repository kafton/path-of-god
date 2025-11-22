"""
Auto-test for skill_6_1_fe408e
"""

from ai_core.skills import skill_6_1_fe408e as skill

def test_skill_6_1_fe408e_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
