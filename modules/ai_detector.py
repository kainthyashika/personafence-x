import re

def detect_ai_text(message: str) -> dict:
    lower = message.lower()

    suspicious_phrases = [
        "as an ai language model",
        "i am not able to",
        "i cannot provide opinions",
        "i was trained on",
        "openai",
        "chatgpt",
        "language model"
    ]

    long_sentences = len([s for s in message.split(".") if len(s) > 120])
    phrase_hits = sum(1 for p in suspicious_phrases if p in lower)
    avg_word_length = sum(len(w) for w in message.split()) / (len(message.split()) + 1)

    score = 0

    if phrase_hits > 0:
        score += 30
    if long_sentences > 2:
        score += 20
    if avg_word_length > 6:
        score += 20
    if re.findall(r"\b(?:however|moreover|furthermore|thus|therefore)\b", lower):
        score += 15

    score = min(score, 100)

    verdict = "🤖 AI-generated" if score > 50 else "👤 Human-written"

    return {
        "ai_score": score,
        "human_score": 100 - score,
        "verdict": verdict
    }
