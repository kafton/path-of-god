"""
Auto-generated test for skill skill_4
"""
from ai_core.skills import skill_4 as skill

def test_skill_4_basic():
    # deterministic test
    assert skill.run(0) == ((0 + 4) * 4)
    assert isinstance(skill.run(1), int)
