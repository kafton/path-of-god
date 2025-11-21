"""
Auto-generated test for skill skill_1
"""
from ai_core.skills import skill_1 as skill

def test_skill_1_basic():
    # deterministic test
    assert skill.run(0) == ((0 + 1) * 1)
    assert isinstance(skill.run(1), int)
