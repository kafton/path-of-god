"""
Auto-test for skill_5_2_923154
"""

from ai_core.skills import skill_5_2_923154 as skill

def test_skill_5_2_923154_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
