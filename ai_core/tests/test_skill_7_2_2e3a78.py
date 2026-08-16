"""
Auto-test for skill_7_2_2e3a78
"""

from ai_core.skills import skill_7_2_2e3a78 as skill

def test_skill_7_2_2e3a78_basic():
    assert skill.run(0) == ((0 + 9) * 9)
    assert isinstance(skill.run(1), int)
