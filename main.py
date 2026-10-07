def word_counter(path: str) -> int:
    words = 0
    with open(path, "r", encoding="utf-8") as file:
        for row in file:
            row = row.strip()
            words += len(row.split(' '))

    return words

if __name__ == "__main__":
    print(word_counter("data/words.txt"))