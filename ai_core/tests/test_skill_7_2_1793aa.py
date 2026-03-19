"""
Auto-test for skill_7_2_1793aa
"""

from ai_core.skills import skill_7_2_1793aa as skill

def test_skill_7_2_1793aa_basic():
    assert skill.run(0) == ((0 + 9) * 9)
    assert isinstance(skill.run(1), int)
