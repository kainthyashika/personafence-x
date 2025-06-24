# modules/detect.py
import json
from utils.txt_style import extract_features

def analyze_message(file_path, user_name):
    try:
        with open(file_path, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        return "[❌] Suspicious file not found."

    input_feat = extract_features(text)

    try:
        with open(f"data/profiles/{user_name}.json", 'r') as f:
            profile = json.load(f)
    except FileNotFoundError:
        return f"[❌] Profile for '{user_name}' not found."

    diffs = {}
    for k in input_feat:
        diffs[k] = abs(input_feat[k] - profile["avg_features"].get(k, 0))

    # Simple score (lower difference → higher score)
    score = 100 - sum(diffs.values()) * 25
    score = max(0, min(100, score))  # Clamp between 0 and 100

    result = f"""
    🔍 Detection Result for '{user_name}':
    - Match Score: {score:.2f}%
    - Verdict: {'⚠️ Possible Impersonation' if score < 80 else '✅ Likely Genuine'}
    """
    return result
