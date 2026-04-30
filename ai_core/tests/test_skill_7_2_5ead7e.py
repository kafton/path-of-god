"""
Auto-test for skill_7_2_5ead7e
"""

from ai_core.skills import skill_7_2_5ead7e as skill

def test_skill_7_2_5ead7e_basic():
    assert skill.run(0) == ((0 + 9) * 9)
    assert isinstance(skill.run(1), int)
