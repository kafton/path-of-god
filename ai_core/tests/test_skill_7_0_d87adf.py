"""
Auto-test for skill_7_0_d87adf
"""

from ai_core.skills import skill_7_0_d87adf as skill

def test_skill_7_0_d87adf_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
