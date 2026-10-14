import re
from collections import Counter

DATA_PATH = "data/words.txt"


def load_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def tokenize(text):
    return [w for w in re.findall(r"\w+", text.lower()) if not w.isdigit()]


def words_for_coverage(counter, target):
    total = sum(counter.values())
    cumulative = 0
    selected = []
    for word, count in counter.most_common():
        cumulative += count
        selected.append(word)
        if cumulative / total >= target:
            break
    return selected, cumulative / total


def main():
    text = load_text(DATA_PATH)
    words = tokenize(text)
    counter = Counter(words)
    total = sum(counter.values())

    print("Liczba slow: {}".format(total))
    print("Unikalne slowa: {}\n".format(len(counter)))

    for target in (0.5, 0.8, 0.9, 0.95, 0.99):
        selected, coverage = words_for_coverage(counter, target)
        print("{:.0%} tekstu pokrywa {:>5} najczestszych slow".format(coverage, len(selected)))

    selected, coverage = words_for_coverage(counter, 0.9)
    print("\nSlowa potrzebne do zrozumienia {:.0%} jezyka ({} slow):".format(coverage, len(selected)))
    print(", ".join(selected))


if __name__ == "__main__":
    main()
