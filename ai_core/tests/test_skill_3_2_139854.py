"""
Auto-test for skill_3_2_139854
"""

from ai_core.skills import skill_3_2_139854 as skill

def test_skill_3_2_139854_basic():
    assert skill.run(0) == ((0 + 5) * 5)
    assert isinstance(skill.run(1), int)
