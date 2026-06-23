"""
Auto-test for skill_7_1_24928e
"""

from ai_core.skills import skill_7_1_24928e as skill

def test_skill_7_1_24928e_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
