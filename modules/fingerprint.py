# modules/fingerprint.py
import os
import json
from utils.txt_style import extract_features

def create_profile(folder_path, user_name):
    features = []
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), 'r') as f:
                text = f.read()
                features.append(extract_features(text))
    avg_profile = {
        "user": user_name,
        "avg_features": {
            k: sum(d[k] for d in features) / len(features)
            for k in features[0]
        }
    }
    os.makedirs("data/profiles", exist_ok=True)
    with open(f"data/profiles/{user_name}.json", "w") as f:
        json.dump(avg_profile, f, indent=4)
    print(f"[✅] Profile created for {user_name}")
