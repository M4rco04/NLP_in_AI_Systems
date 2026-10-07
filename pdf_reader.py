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

    args = parser.parse_args()

    # data/hans_christian_andersen.pdf, 6, 125
    book = read_pdf(args.pdf_path, args.start, args.end)
    book_clean = re.sub(r'[<>"\-()!?.,:\;\»\«]', '', book)

    with open("data/words.txt", "a", encoding="utf-8") as w:
        w.write(book_clean)