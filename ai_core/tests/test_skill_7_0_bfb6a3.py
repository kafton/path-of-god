"""
Auto-test for skill_7_0_bfb6a3
"""

from ai_core.skills import skill_7_0_bfb6a3 as skill

def test_skill_7_0_bfb6a3_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
