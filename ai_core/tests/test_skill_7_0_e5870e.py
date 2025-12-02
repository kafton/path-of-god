"""
Auto-test for skill_7_0_e5870e
"""

from ai_core.skills import skill_7_0_e5870e as skill

def test_skill_7_0_e5870e_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
