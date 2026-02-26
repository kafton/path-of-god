"""
Auto-test for skill_7_2_c39c99
"""

from ai_core.skills import skill_7_2_c39c99 as skill

def test_skill_7_2_c39c99_basic():
    assert skill.run(0) == ((0 + 9) * 9)
    assert isinstance(skill.run(1), int)
