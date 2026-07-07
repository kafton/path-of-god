"""
Auto-test for skill_7_1_6ef492
"""

from ai_core.skills import skill_7_1_6ef492 as skill

def test_skill_7_1_6ef492_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
