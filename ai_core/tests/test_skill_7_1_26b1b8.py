"""
Auto-test for skill_7_1_26b1b8
"""

from ai_core.skills import skill_7_1_26b1b8 as skill

def test_skill_7_1_26b1b8_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
