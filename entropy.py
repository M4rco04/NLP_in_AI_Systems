import re
import math
from collections import Counter

DATA_PATH = "data/words.txt"


def load_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def tokenize(text):
    return [w for w in re.findall(r"\w+", text.lower()) if not w.isdigit()]


def entropy(counter):
    total = sum(counter.values())
    if total == 0:
        return 0.0
    return -sum((count / total) * math.log2(count / total) for count in counter.values())


def main():
    text = load_text(DATA_PATH)
    words = tokenize(text)
    chars = [c for c in text.lower() if not c.isspace()]

    word_counter = Counter(words)
    char_counter = Counter(chars)

    word_entropy = entropy(word_counter)
    char_entropy = entropy(char_counter)

    unique_words = len(word_counter)
    max_word_entropy = math.log2(unique_words) if unique_words else 0.0

    print("Liczba slow: {}".format(len(words)))
    print("Unikalne slowa: {}".format(unique_words))
    print("Entropia slow (Shannon): {:.4f} bit".format(word_entropy))
    print("Maksymalna entropia slow: {:.4f} bit".format(max_word_entropy))
    if max_word_entropy:
        print("Nadmiarowosc slow: {:.2%}".format(1 - word_entropy / max_word_entropy))
    print("Entropia znakow: {:.4f} bit".format(char_entropy))


if __name__ == "__main__":
    main()
