"""
Auto-test for skill_7_1_a28952
"""

from ai_core.skills import skill_7_1_a28952 as skill

def test_skill_7_1_a28952_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
