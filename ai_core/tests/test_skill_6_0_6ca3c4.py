"""
Auto-test for skill_6_0_6ca3c4
"""

from ai_core.skills import skill_6_0_6ca3c4 as skill

def test_skill_6_0_6ca3c4_basic():
    assert skill.run(0) == ((0 + 6) * 6)
    assert isinstance(skill.run(1), int)
