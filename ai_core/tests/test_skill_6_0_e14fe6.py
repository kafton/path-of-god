"""
Auto-test for skill_6_0_e14fe6
"""

from ai_core.skills import skill_6_0_e14fe6 as skill

def test_skill_6_0_e14fe6_basic():
    assert skill.run(0) == ((0 + 6) * 6)
    assert isinstance(skill.run(1), int)
