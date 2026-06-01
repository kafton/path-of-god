"""
Auto-test for skill_7_0_5d0d81
"""

from ai_core.skills import skill_7_0_5d0d81 as skill

def test_skill_7_0_5d0d81_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
