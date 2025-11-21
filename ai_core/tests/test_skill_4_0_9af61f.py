"""
Auto-test for skill_4_0_9af61f
"""

from ai_core.skills import skill_4_0_9af61f as skill

def test_skill_4_0_9af61f_basic():
    assert skill.run(0) == ((0 + 4) * 4)
    assert isinstance(skill.run(1), int)
