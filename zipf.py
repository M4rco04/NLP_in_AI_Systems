import re
import math
from collections import Counter

DATA_PATH = "data/words.txt"


def load_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def tokenize(text):
    return [w for w in re.findall(r"\w+", text.lower()) if not w.isdigit()]


def linear_regression(xs, ys):
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    sxx = sum((x - mean_x) ** 2 for x in xs)
    sxy = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    slope = sxy / sxx
    intercept = mean_y - slope * mean_x

    ss_tot = sum((y - mean_y) ** 2 for y in ys)
    ss_res = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(xs, ys))
    r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
    return slope, intercept, r2


def main():
    text = load_text(DATA_PATH)
    words = tokenize(text)
    counter = Counter(words)

    frequencies = [count for _, count in counter.most_common()]
    ranks = list(range(1, len(frequencies) + 1))

    xs = [math.log(rank) for rank in ranks]
    ys = [math.log(freq) for freq in frequencies]

    slope, intercept, r2 = linear_regression(xs, ys)

    print("Unikalne slowa: {}".format(len(frequencies)))
    print("Nachylenie log-log (Zipf): {:.4f}".format(slope))
    print("Wspolczynnik R^2: {:.4f}".format(r2))
    print("Stala wykladnicza: {:.4f}".format(-slope))
    if -1.1 <= slope <= -0.9:
        print("Wniosek: dane spelniaja prawo Zipfa (nachylenie blisko -1).")
    else:
        print("Wniosek: dane odbiegaja od klasycznego prawa Zipfa.")

    print("\nNajczestsze slowa (ranga, wystapienia, iloczyn):")
    for rank in range(1, min(21, len(frequencies) + 1)):
        word, count = counter.most_common(rank)[-1]
        print("{:>4}. {:<15} {:>8} {:>12.0f}".format(rank, word, count, rank * count))


if __name__ == "__main__":
    main()
