"""
Auto-test for skill_6_1_ed0c13
"""

from ai_core.skills import skill_6_1_ed0c13 as skill

def test_skill_6_1_ed0c13_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
