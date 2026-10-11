from pathlib import Path
import json
import fitz

PDF_DIR = Path("data/pdfs")
OUTPUT_FILE = Path("data/processed/extracted_pages.json")


def main():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    pdf_files = sorted(PDF_DIR.glob("*.pdf"))
    all_pages = []

    if not pdf_files:
        raise FileNotFoundError(f"No PDFs found in {PDF_DIR.resolve()}")

    for pdf_path in pdf_files:
        try:
            with fitz.open(pdf_path) as pdf:
                readable_pages = 0

                for page_number, page in enumerate(pdf, start=1):
                    text = page.get_text("text").strip()
                    if text:
                        readable_pages += 1

                    all_pages.append({
                        "source": pdf_path.name,
                        "page": page_number,
                        "text": text
                    })

                print(
                    f"{pdf_path.name}: "
                    f"{readable_pages}/{len(pdf)} pages contain text"
                )

        except Exception as error:
            print(f"Failed: {pdf_path.name}: {error}")

    OUTPUT_FILE.write_text(
        json.dumps(all_pages, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"\nPDFs found: {len(pdf_files)}")
    print(f"Pages processed: {len(all_pages)}")
    print(f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
