"""
Auto-test for skill_7_2_fc92ec
"""

from ai_core.skills import skill_7_2_fc92ec as skill

def test_skill_7_2_fc92ec_basic():
    assert skill.run(0) == ((0 + 9) * 9)
    assert isinstance(skill.run(1), int)
