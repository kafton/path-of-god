"""
Auto-test for skill_7_1_1a6a15
"""

from ai_core.skills import skill_7_1_1a6a15 as skill

def test_skill_7_1_1a6a15_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
