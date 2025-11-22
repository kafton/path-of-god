"""
Auto-test for skill_5_0_c35fab
"""

from ai_core.skills import skill_5_0_c35fab as skill

def test_skill_5_0_c35fab_basic():
    assert skill.run(0) == ((0 + 5) * 5)
    assert isinstance(skill.run(1), int)
