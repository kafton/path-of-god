"""
Auto-test for skill_7_0_8333dd
"""

from ai_core.skills import skill_7_0_8333dd as skill

def test_skill_7_0_8333dd_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
