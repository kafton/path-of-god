"""
Auto-test for skill_5_1_1897c8
"""

from ai_core.skills import skill_5_1_1897c8 as skill

def test_skill_5_1_1897c8_basic():
    assert skill.run(0) == ((0 + 6) * 6)
    assert isinstance(skill.run(1), int)
