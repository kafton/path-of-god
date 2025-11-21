#!/usr/bin/env python3
"""
self_evolver_v2.py
Advanced safe evolver:
- Multi-file candidate generation
- Personality-driven candidate bias
- Mutation + selection via unit tests and heuristics
- Writes only inside ai_core/
- Outputs minimal metadata for workflow
"""

import os
import json
import random
import uuid
import shutil
import subprocess
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AI_DIR = os.path.join(BASE_DIR, "ai_core")
SKILLS_DIR = os.path.join(AI_DIR, "skills")
CANDIDATES_DIR = os.path.join(AI_DIR, "candidates")
TESTS_DIR = os.path.join(AI_DIR, "tests")
MEMORY_FILE = os.path.join(AI_DIR, "ai_memory.json")
PERSONALITY_FILE = os.path.join(AI_DIR, "personality.json")
MUTATION_MODULE = os.path.join(AI_DIR, "mutation.py")

# Safety prefix for allowed writes
ALLOWED_PREFIX = os.path.normpath(AI_DIR)

# Ensure dirs exist
def ensure_dirs():
    os.makedirs(SKILLS_DIR, exist_ok=True)
    os.makedirs(CANDIDATES_DIR, exist_ok=True)
    os.makedirs(TESTS_DIR, exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({"runs": [], "skills": []}, f, indent=2)
    if not os.path.exists(PERSONALITY_FILE):
        # default personality: optimizer
        default = {"type": "optimizer", "goal": "maximize_numeric_scores", "bias_strength": 1.0}
        with open(PERSONALITY_FILE, "w") as f:
            json.dump(default, f, indent=2)
    if not os.path.exists(MUTATION_MODULE):
        # create a minimal mutation module (safe)
        with open(MUTATION_MODULE, "w") as f:
            f.write("# safe mutation helpers\n\ndef minor_mutation(code, level):\n    # This simple mutation changes the numeric constant 'level' used inside code\n    return code.replace(f'Level: {level}', f'Level: {max(1, level+1)}')\n")

def is_safe(path):
    return os.path.normpath(path).startswith(ALLOWED_PREFIX)

def write_safe(path, content):
    if not is_safe(path):
        raise RuntimeError(f"Unsafe write: {path}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def load_memory():
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(m):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(m, f, indent=2)

def load_personality():
    with open(PERSONALITY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Simple deterministic skill template (testable)
def generate_skill_template(name, level, personality):
    # personality can adjust behavior/description
    desc = f"Auto-generated skill {name} (Level: {level})"
    if personality.get("type") == "storyteller":
        desc += " - story-focused"
    elif personality.get("type") == "helper":
        desc += " - helper utility"
    elif personality.get("type") == "optimizer":
        desc += " - optimizer heuristic"
    code = f'''"""
Auto-generated skill: {name}
Level: {level}
Generated: {datetime.utcnow().isoformat()}Z
Description: {desc}
"""
def info():
    return {{"name":"{name}","level":{level},"desc":"{desc}"}}

def run(x: int) -> int:
    # deterministic scoring function (testable)
    return max(0, (x + {level}) * {level})
'''
    return code

def generate_test(name, level):
    test = f'''"""
Auto-test for {name}
"""
from ai_core.skills import {name} as skill

def test_{name}_basic():
    assert skill.run(0) == ((0 + {level}) * {level})
    assert isinstance(skill.run(1), int)
'''
    return test

def run_pytest_on_tests(test_dir):
    # run pytest, return (passed_count, total_count) via exit code parsing
    try:
        res = subprocess.run(["pytest", "-q", test_dir], capture_output=True, text=True, check=False)
        out = res.stdout + "\n" + res.stderr
        # simple parse: look for '== X passed' patterns
        passed = 0
        total = 0
        for line in out.splitlines():
            if "passed" in line and "failed" not in line:
                # line like "1 passed"
                parts = line.strip().split()
                for i,p in enumerate(parts):
                    if p == "passed":
                        try:
                            passed = int(parts[i-1])
                        except:
                            pass
            if "collected" in line:
                try:
                    total = int(line.split()[1])
                except:
                    pass
        # fallback: if pytest exit code 0, assume pass
        if res.returncode == 0 and total==0:
            passed = 1; total = 1
        return max(0, passed), max(0, total), res.returncode, out
    except Exception as e:
        return 0, 0, 1, str(e)

def score_candidate(passed, total, level, personality):
    # Score is weighted by tests passing + personality heuristic
    base = (passed / total) if total>0 else 0
    # personality bias: e.g., favor higher level for optimizer
    bias = 0.0
    ptype = personality.get("type", "optimizer")
    if ptype == "optimizer":
        bias = min(1.0, level/10.0) * personality.get("bias_strength", 1.0)
    elif ptype == "storyteller":
        bias = 0.1
    elif ptype == "helper":
        bias = 0.2
    return base + bias

def propose_and_test_candidates(num_candidates=3):
    memory = load_memory()
    personality = load_personality()
    candidates = []
    next_level = 1 + len(memory.get("skills", []))
    for i in range(num_candidates):
        name = f"skill_{next_level}_{i}_{uuid.uuid4().hex[:6]}"
        level = next_level + i  # simple variance
        code = generate_skill_template(name, level, personality)
        test = generate_test(name, level)
        cand_dir = os.path.join(CANDIDATES_DIR, name)
        os.makedirs(cand_dir, exist_ok=True)
        skill_path = os.path.join(cand_dir, f"{name}.py")
        test_path = os.path.join(TESTS_DIR, f"test_{name}.py")
        write_safe(skill_path, code)
        write_safe(test_path, test)
        # temporarily copy candidate into ai_core/skills to run tests in package context
        temp_skill_dest = os.path.join(SKILLS_DIR, f"{name}.py")
        shutil.copyfile(skill_path, temp_skill_dest)
        passed, total, rc, out = run_pytest_on_tests(TESTS_DIR)
        # cleanup temp skill file
        os.remove(temp_skill_dest)
        score = score_candidate(passed, total if total>0 else 1, level, personality)
        candidates.append({
            "name": name, "level": level, "skill_path": skill_path,
            "test_path": test_path, "passed": passed, "total": total, "rc": rc, "score": score, "output": out
        })
    return candidates

def promote_best_candidate(candidates):
    if not candidates:
        return None
    # choose highest score
    best = max(candidates, key=lambda c: c["score"])
    # move candidate file into skills/
    src_skill = best["skill_path"]
    dst_skill = os.path.join(SKILLS_DIR, os.path.basename(src_skill))
    shutil.copyfile(src_skill, dst_skill)
    # move its test into tests/ (overwrite if exists)
    dst_test = os.path.join(TESTS_DIR, os.path.basename(best["test_path"]))
    shutil.copyfile(best["test_path"], dst_test)
    # record in memory
    memory = load_memory()
    memory.setdefault("skills", []).append({
        "name": best["name"], "level": best["level"], "promoted_at": datetime.utcnow().isoformat()+"Z"
    })
    memory.setdefault("runs", []).append({
        "time": datetime.utcnow().isoformat()+"Z", "action":"promote_best", "candidate": best["name"], "score": best["score"]
    })
    save_memory(memory)
    return best

def main():
    ensure_dirs()
    print("[evolver] start run:", datetime.utcnow().isoformat()+"Z")
    # generate & test candidates
    candidates = propose_and_test_candidates(num_candidates=3)
    for c in candidates:
        print(f"[candidate] {c['name']} pass={c['passed']}/{c['total']} score={c['score']:.3f} rc={c['rc']}")
    # promote best
    best = promote_best_candidate(candidates)
    if best:
        print("[evolver] promoted:", best["name"], "score:", best["score"])
        # print metadata JSON for workflow
        print(json.dumps({"promoted": best["name"], "score": best["score"]}))
    else:
        print("[evolver] no candidate promoted")
    print("[evolver] end run")

if __name__ == "__main__":
    main()
