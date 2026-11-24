"""
Auto-test for skill_7_2_c4a528
"""

from ai_core.skills import skill_7_2_c4a528 as skill

def test_skill_7_2_c4a528_basic():
    assert skill.run(0) == ((0 + 9) * 9)
    assert isinstance(skill.run(1), int)
