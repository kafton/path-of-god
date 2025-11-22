"""
Auto-generated test for skill skill_5
"""
from ai_core.skills import skill_5 as skill

def test_skill_5_basic():
    # deterministic test
    assert skill.run(0) == ((0 + 5) * 5)
    assert isinstance(skill.run(1), int)
