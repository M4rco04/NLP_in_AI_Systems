import pymupdf
import re
import argparse

def read_pdf(path: str, start_page: int, end_page: int) -> str:
    doc = pymupdf.open(path)
    text = ""

    for page_nb in range(start_page, end_page):
        page = doc.load_page(page_nb)
        text += page.get_text()

    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="download the PDF text and write it into a txt file")
    parser.add_argument("pdf_path", type=str, help="PDF file path")
    parser.add_argument("start", type=int, help="Start page")
    parser.add_argument("end", type=int, help="End page")
    parser.add_argument("-o", "--out", type=str, default="data/words.txt", help="Output txt file")
    parser.add_argument("--append", action="store_true", help="Append instead of overwrite")

    args = parser.parse_args()

    # data/hans_christian_andersen.pdf, 6, 125
    # data/tom_sawyer.pdf, 5, 286
    book = read_pdf(args.pdf_path, args.start, args.end)

    book_clean = re.sub(r"-\s*\n\s*", "-", book)
    book_clean = re.sub(r"(?<!\S)-|-(?!\S)", " ", book_clean)
    book_clean = re.sub(r"[^\w\s'’·-]", " ", book_clean, flags=re.UNICODE)
    book_clean = re.sub(r"\b\d[\d-]*\b", " ", book_clean)
    book_clean = re.sub(r"\s*-\s*", "-", book_clean)
    book_clean = re.sub(r"\s+", " ", book_clean).strip()

    with open(args.out, "a" if args.append else "w", encoding="utf-8") as w:
        if args.append:
            w.write("\n")
        w.write(book_clean)