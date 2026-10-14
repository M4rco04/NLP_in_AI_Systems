import re
from collections import Counter, defaultdict

DATA_PATH = "data/words.txt"
WINDOW = 5
MIN_COUNT = 20


def load_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def tokenize(text):
    return [w for w in re.findall(r"\w+", text.lower()) if not w.isdigit()]


def build_neighbors(words, window, min_count):
    frequency = Counter(words)
    neighbors = defaultdict(set)

    for i, word in enumerate(words):
        if frequency[word] < min_count:
            continue
        for j in range(i + 1, min(i + window + 1, len(words))):
            other = words[j]
            if other == word or frequency[other] < min_count:
                continue
            neighbors[word].add(other)
            neighbors[other].add(word)

    return neighbors, frequency


def main():
    text = load_text(DATA_PATH)
    words = tokenize(text)
    neighbors, frequency = build_neighbors(words, WINDOW, MIN_COUNT)

    ranked = sorted(neighbors.items(), key=lambda item: len(item[1]), reverse=True)

    print("Okno wspolwystepowania: {} slow".format(WINDOW))
    print("Minimalna liczba wystapien: {}".format(MIN_COUNT))
    print("Slowo w rdzeniu: {} (z {} unikalnych)\n".format(len(ranked), len(frequency)))

    print("Rdzen jezyka - slowa z najwieksza liczba sasiadow:")
    print("{:>4}  {:<15} {:>10} {:>10}".format("Msc", "Slowo", "Sasiedzi", "Wystapien"))
    for i, (word, neigh) in enumerate(ranked[:30], start=1):
        print("{:>4}  {:<15} {:>10} {:>10}".format(i, word, len(neigh), frequency[word]))


if __name__ == "__main__":
    main()
