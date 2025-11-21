"""
Auto-test for skill_3_1_71773e
"""

from ai_core.skills import skill_3_1_71773e as skill

def test_skill_3_1_71773e_basic():
    assert skill.run(0) == ((0 + 4) * 4)
    assert isinstance(skill.run(1), int)
