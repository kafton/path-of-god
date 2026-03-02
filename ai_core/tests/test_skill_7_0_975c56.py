"""
Auto-test for skill_7_0_975c56
"""

from ai_core.skills import skill_7_0_975c56 as skill

def test_skill_7_0_975c56_basic():
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
