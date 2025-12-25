"""
Auto-test for skill_7_1_7aa889
"""

from ai_core.skills import skill_7_1_7aa889 as skill

def test_skill_7_1_7aa889_basic():
    assert skill.run(0) == ((0 + 8) * 8)
    assert isinstance(skill.run(1), int)
