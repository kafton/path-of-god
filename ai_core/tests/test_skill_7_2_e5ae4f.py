"""
Auto-test for skill_7_2_e5ae4f
"""

from ai_core.skills import skill_7_2_e5ae4f as skill

def test_skill_7_2_e5ae4f_basic():
    assert skill.run(0) == ((0 + 9) * 9)
    assert isinstance(skill.run(1), int)
