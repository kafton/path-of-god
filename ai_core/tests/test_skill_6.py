"""
Auto-generated test for skill skill_6
"""
from ai_core.skills import skill_6 as skill

def test_skill_6_basic():
    # deterministic test
    assert skill.run(0) == ((0 + 6) * 6)
    assert isinstance(skill.run(1), int)
