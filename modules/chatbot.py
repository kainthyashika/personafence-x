import os
import random

def load_profile_phrases(profile_name):
    profile_dir = f"profiles/{profile_name}"
    phrases = []

    if not os.path.exists(profile_dir):
        print("❌ Profile not found.")
        return phrases

    for file in os.listdir(profile_dir):
        if file.endswith(".txt"):
            with open(os.path.join(profile_dir, file), "r") as f:
                lines = f.readlines()
                phrases.extend([line.strip() for line in lines if len(line.strip()) > 10])

    return phrases

def start_chat(profile_name):
    print(f"\n💬 PersonaFence ChatBot: Emulating {profile_name}")
    print("Type 'exit' to stop chatting.\n")

    phrases = load_profile_phrases(profile_name)
    if not phrases:
        print("⚠️ No phrases found to simulate chat.")
        return

    while True:
        msg = input("👤 You: ").strip()
        if msg.lower() in ["exit", "quit"]:
            print("👋 Exiting ChatBot.\n")
            break
        reply = random.choice(phrases)
        print(f"🤖 {profile_name}: {reply}\n")
