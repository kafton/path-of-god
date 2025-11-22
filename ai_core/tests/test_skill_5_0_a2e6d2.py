"""
Auto-test for skill_5_0_a2e6d2
"""

from ai_core.skills import skill_5_0_a2e6d2 as skill

def test_skill_5_0_a2e6d2_basic():
    assert skill.run(0) == ((0 + 5) * 5)
    assert isinstance(skill.run(1), int)
