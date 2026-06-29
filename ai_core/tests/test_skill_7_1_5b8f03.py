"""
Auto-test for skill_7_1_5b8f03
"""

from ai_core.skills import skill_7_1_5b8f03 as skill

def test_skill_7_1_5b8f03_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
