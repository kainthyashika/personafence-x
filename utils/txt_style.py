# utils/text_style.py
import re
import numpy as np

def extract_features(text):
    words = text.split()
    sentences = re.split(r'[.!?]', text)
    avg_word_len = np.mean([len(w) for w in words])
    avg_sentence_len = np.mean([len(s.split()) for s in sentences if s.strip()])
    punctuation_freq = text.count('!') + text.count('?')
    vocab_richness = len(set(words)) / len(words) if words else 0

    return {
        "avg_word_length": avg_word_len,
        "avg_sentence_length": avg_sentence_len,
        "punctuation_freq": punctuation_freq,
        "vocab_richness": vocab_richness
    }
