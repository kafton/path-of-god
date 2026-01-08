"""
Auto-test for skill_7_1_8d71d1
"""

from ai_core.skills import skill_7_1_8d71d1 as skill

def test_skill_7_1_8d71d1_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
