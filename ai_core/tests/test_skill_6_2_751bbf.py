"""
Auto-test for skill_6_2_751bbf
"""

from ai_core.skills import skill_6_2_751bbf as skill

def test_skill_6_2_751bbf_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
