# Generative AI RAG Dataset

A Python data pipeline for AI, LLM, and generative AI research documents.

## Dataset
- 14 PDF documents
- 738 pages extracted
- 3,925 text chunks generated

## Pipeline
- PDF text extraction using PyMuPDF
- Text chunking with overlap
- Source filename and page metadata

## Project Structure
- data/pdfs/ — Original PDFs
- data/processed/ — Extracted pages and chunks
- src/extract_text.py — PDF extraction
- src/chunk_documents.py — Text chunking

## Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Run
python src/extract_text.py
python src/chunk_documents.py

## Next Steps
- Generate embeddings
- Create a FAISS vector index
- Implement semantic retrieval
- Evaluate retrieval quality
