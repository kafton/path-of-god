"""
Auto-test for skill_7_1_f81c23
"""

from ai_core.skills import skill_7_1_f81c23 as skill

def test_skill_7_1_f81c23_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
