"""
Auto-generated test for skill skill_7
"""
from ai_core.skills import skill_7 as skill

def test_skill_7_basic():
    # deterministic test
    assert skill.run(0) == ((0 + 7) * 7)
    assert isinstance(skill.run(1), int)
