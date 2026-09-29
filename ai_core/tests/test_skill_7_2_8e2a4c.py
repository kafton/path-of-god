"""
Auto-test for skill_7_2_8e2a4c
"""

from ai_core.skills import skill_7_2_8e2a4c as skill

def test_skill_7_2_8e2a4c_basic():
    assert skill.run(0) == ((0 + 9) * 9)
    assert isinstance(skill.run(1), int)
