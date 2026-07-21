"""
Auto-test for skill_7_1_ba3d6e
"""

from ai_core.skills import skill_7_1_ba3d6e as skill

def test_skill_7_1_ba3d6e_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
