"""
Auto-test for skill_7_0_273bbb
"""

from ai_core.skills import skill_7_0_273bbb as skill

def test_skill_7_0_273bbb_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
