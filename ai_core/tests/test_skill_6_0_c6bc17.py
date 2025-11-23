"""
Auto-test for skill_6_0_c6bc17
"""

from ai_core.skills import skill_6_0_c6bc17 as skill

def test_skill_6_0_c6bc17_basic():
    assert skill.run(0) == ((0 + 6) * 6)
    assert isinstance(skill.run(1), int)
