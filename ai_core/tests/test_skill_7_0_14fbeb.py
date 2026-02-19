"""
Auto-test for skill_7_0_14fbeb
"""

from ai_core.skills import skill_7_0_14fbeb as skill

def test_skill_7_0_14fbeb_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
