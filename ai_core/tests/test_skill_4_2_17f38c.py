"""
Auto-test for skill_4_2_17f38c
"""

from ai_core.skills import skill_4_2_17f38c as skill

def test_skill_4_2_17f38c_basic():
    assert skill.run(0) == ((0 + 6) * 6)
    assert isinstance(skill.run(1), int)
