"""
Auto-generated test for skill skill_2
"""
from ai_core.skills import skill_2 as skill

def test_skill_2_basic():
    # deterministic test
    assert skill.run(0) == ((0 + 2) * 2)
    assert isinstance(skill.run(1), int)
