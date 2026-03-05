"""
Auto-test for skill_7_1_3c6e04
"""

from ai_core.skills import skill_7_1_3c6e04 as skill

def test_skill_7_1_3c6e04_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
