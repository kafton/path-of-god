"""
Auto-test for skill_7_0_c09e2d
"""

from ai_core.skills import skill_7_0_c09e2d as skill

def test_skill_7_0_c09e2d_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
