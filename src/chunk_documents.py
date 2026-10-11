from pathlib import Path
import json
import re

INPUT_FILE = Path("data/processed/extracted_pages.json")
OUTPUT_FILE = Path("data/processed/chunks.json")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150


def split_text(text):
    text = re.sub(r"\s+", " ", text).strip()

    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + CHUNK_SIZE, len(text))

        if end < len(text):
            boundary = text.rfind(" ", start, end)
            if boundary > start:
                end = boundary

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        next_start = max(start + 1, end - CHUNK_OVERLAP)
        space = text.find(" ", next_start, end)

        if space != -1:
            next_start = space + 1

        start = next_start

    return chunks


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Extract the PDFs first: {INPUT_FILE}"
        )

    pages = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    all_chunks = []
    chunk_id = 0

    for page in pages:
        for index, content in enumerate(split_text(page.get("text", ""))):
            all_chunks.append({
                "chunk_id": chunk_id,
                "source": page["source"],
                "page": page["page"],
                "chunk_index": index,
                "text": content
            })
            chunk_id += 1

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(all_chunks, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"Pages read: {len(pages)}")
    print(f"Chunks created: {len(all_chunks)}")
    print(f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
