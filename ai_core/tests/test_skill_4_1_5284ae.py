"""
Auto-test for skill_4_1_5284ae
"""

from ai_core.skills import skill_4_1_5284ae as skill

def test_skill_4_1_5284ae_basic():
    assert skill.run(0) == ((0 + 5) * 5)
    assert isinstance(skill.run(1), int)
