# self_rewriting_ai.py
# Safe educational AI that learns and rewrites itself
import re
import random

# Knowledge base (what AI can "rewrite")
knowledge_score = 5  # AI will adjust this value as it learns

def environment_feedback(score):
    """Simulated environment feedback"""
    # Reward is higher if score is near 10, lower if far
    ideal = 10
    reward = max(0, 10 - abs(ideal - score))
    # Add randomness to simulate environment variability
    reward += random.randint(-2, 2)
    reward = max(0, reward)
    return reward

def learn():
    """AI decides whether to change knowledge_score"""
    global knowledge_score
    reward = environment_feedback(knowledge_score)
    print(f"Current knowledge_score: {knowledge_score}, reward: {reward}")

    # Simple learning rule
    if reward < 5:
        knowledge_score += 1
        print("AI increases knowledge_score")
    elif reward > 8 and knowledge_score > 0:
        knowledge_score -= 1
        print("AI decreases knowledge_score")
    else:
        print("AI keeps knowledge_score the same")

def rewrite_self():
    """Rewrite the script with updated knowledge_score"""
    file_path = __file__
    with open(file_path, "r") as f:
        code = f.read()
    new_code = re.sub(
        r"knowledge_score = (\d+)",
        f"knowledge_score = {knowledge_score}",
        code
    )
    with open(file_path, "w") as f:
        f.write(new_code)

def main():
    learn()
    rewrite_self()
    print(f"AI updated itself! New knowledge_score = {knowledge_score}")

if __name__ == "__main__":
    main()
