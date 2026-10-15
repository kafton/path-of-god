"""
Auto-test for skill_7_2_1cee13
"""

from ai_core.skills import skill_7_2_1cee13 as skill

def test_skill_7_2_1cee13_basic():
    assert skill.run(0) == ((0 + 9) * 9)
    assert isinstance(skill.run(1), int)
