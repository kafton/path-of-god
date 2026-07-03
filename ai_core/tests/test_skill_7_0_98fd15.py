"""
Auto-test for skill_7_0_98fd15
"""

from ai_core.skills import skill_7_0_98fd15 as skill

def test_skill_7_0_98fd15_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
