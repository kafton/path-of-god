"""
Auto-test for skill_7_0_a4e2ed
"""

from ai_core.skills import skill_7_0_a4e2ed as skill

def test_skill_7_0_a4e2ed_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
