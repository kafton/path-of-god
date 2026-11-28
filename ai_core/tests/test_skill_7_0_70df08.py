"""
Auto-test for skill_7_0_70df08
"""

from ai_core.skills import skill_7_0_70df08 as skill

def test_skill_7_0_70df08_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
