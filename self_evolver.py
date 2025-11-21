#!/usr/bin/env python3
"""
self_evolver.py
Safe "advanced mode" evolver:
- Generates new skill modules under ai_core/skills/
- Generates basic unit tests for the new skill under ai_core/tests/
- Writes ai_memory.json for tracking
- Never writes outside ai_core/ (safety check)
- Does NOT push/PR itself — the GitHub workflow will commit, push, and create the PR
"""

import os
import json
import re
from datetime import datetime
import random
import uuid

# --- CONFIG ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AI_DIR = os.path.join(BASE_DIR, "ai_core")
SKILLS_DIR = os.path.join(AI_DIR, "skills")
TESTS_DIR = os.path.join(AI_DIR, "tests")
MEMORY_FILE = os.path.join(AI_DIR, "ai_memory.json")

ALLOWED_DIR_PREFIX = os.path.normpath(AI_DIR)  # safety: only allow writes inside this dir

# --- SAFETY HELPERS ---
def ensure_dirs():
    os.makedirs(SKILLS_DIR, exist_ok=True)
    os.makedirs(TESTS_DIR, exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({"runs": [], "skills": []}, f, indent=2)

def is_safe_path(path):
    # Normalize and ensure path is inside ai_core
    norm = os.path.normpath(path)
    return norm.startswith(ALLOWED_DIR_PREFIX)

def write_file_safe(path, content):
    if not is_safe_path(path):
        raise RuntimeError(f"Unsafe write attempted: {path}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# --- MEMORY ---
def load_memory():
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(m):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(m, f, indent=2)

# --- SKILL GENERATOR ---
def generate_skill_code(name, level):
    """Return Python code for a new simple skill."""
    code = f'''"""
Auto-generated skill: {name}
Level: {level}
Generated: {datetime.utcnow().isoformat()}Z
"""

def info():
    return {{
        "name": "{name}",
        "level": {level},
        "desc": "Auto-generated skill that computes an integer score."
    }}

def run(input_value: int) -> int:
    """
    Simple deterministic function that returns an integer score.
    This is intentionally simple and testable.
    """
    # skill behavior scales with level
    return max(0, (input_value + {level}) * {level})
'''
    return code

def generate_test_code(name, level):
    """Return a pytest unit test for the generated skill."""
    test = f'''"""
Auto-generated test for skill {name}
"""
from ai_core.skills import {name} as skill

def test_{name}_basic():
    # deterministic test
    assert skill.run(0) == ((0 + {level}) * {level})
    assert isinstance(skill.run(1), int)
'''
    return test

# --- MAIN EVOLUTION STEP ---
def propose_new_skill():
    # Simple heuristic: create a new skill occasionally with incremental level
    memory = load_memory()
    next_level = 1 + len(memory.get("skills", []))
    skill_name = f"skill_{next_level}"
    # ensure unique
    if any(s["name"] == skill_name for s in memory.get("skills", [])):
        # fallback to uuid name
        skill_name = f"skill_{next_level}_{uuid.uuid4().hex[:6]}"

    code = generate_skill_code(skill_name, next_level)
    test = generate_test_code(skill_name, next_level)

    # safety filenames
    skill_path = os.path.join(SKILLS_DIR, f"{skill_name}.py")
    test_path = os.path.join(TESTS_DIR, f"test_{skill_name}.py")

    write_file_safe(skill_path, code)
    write_file_safe(test_path, test)

    # update memory
    memory["skills"].append({
        "name": skill_name,
        "level": next_level,
        "created": datetime.utcnow().isoformat() + "Z"
    })
    memory["runs"].append({
        "time": datetime.utcnow().isoformat() + "Z",
        "action": "propose_new_skill",
        "skill": skill_name
    })
    save_memory(memory)

    print(f"[Evolver] Proposed skill {skill_name} (level {next_level})")
    return skill_name, skill_path, test_path

def main():
    ensure_dirs()
    print("AI Evolver starting...")

    # maybe mutate an existing skill instead of creating new one
    memory = load_memory()
    action = random.choice(["new_skill", "mutate_skill", "noop"])
    # bias towards new_skill
    if random.random() < 0.6:
        action = "new_skill"

    if action == "new_skill":
        skill_name, skill_path, test_path = propose_new_skill()
        print("Wrote:", skill_path, test_path)
        # output metadata for workflow
        meta = {"skill": skill_name}
        print(json.dumps(meta))
    elif action == "mutate_skill" and memory.get("skills"):
        # Simple mutation: bump level and rewrite file
        s = random.choice(memory["skills"])
        new_level = s["level"] + 1
        code = generate_skill_code(s["name"], new_level)
        skill_path = os.path.join(SKILLS_DIR, f"{s['name']}.py")
        write_file_safe(skill_path, code)
        s["level"] = new_level
        s["mutated_at"] = datetime.utcnow().isoformat() + "Z"
        memory["runs"].append({"time": datetime.utcnow().isoformat() + "Z", "action": "mutate_skill", "skill": s["name"], "new_level": new_level})
        save_memory(memory)
        print(f"[Evolver] Mutated {s['name']} -> level {new_level}")
    else:
        print("[Evolver] No action this run.")
        memory["runs"].append({"time": datetime.utcnow().isoformat() + "Z", "action": "noop"})
        save_memory(memory)

if __name__ == "__main__":
    main()
