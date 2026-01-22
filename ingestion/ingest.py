import os
import fitz  # PyMuPDF
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "..", "data", "pdfs", "sample.pdf")


def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []

    for page_num, page in enumerate(doc):
        text = page.get_text()
        pages.append({
            "page": page_num + 1,
            "text": text
        })

    return pages


def chunk_pages(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=120
    )

    chunks = []

    for page in pages:
        page_chunks = splitter.split_text(page["text"])
        for chunk in page_chunks:
            chunks.append({
                "text": chunk,
                "metadata": {
                    "page": page["page"],
                    "source": "sample.pdf"
                }
            })

    return chunks


def store_embeddings(chunks):
    client = chromadb.Client()
    collection = client.create_collection(name="documind")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk["text"]).tolist()

        collection.add(
            ids=[str(i)],
            documents=[chunk["text"]],
            metadatas=[chunk["metadata"]],
            embeddings=[embedding]
        )

    return collection


# 🔴 THIS FUNCTION WAS MISSING OR NOT DEFINED PROPERLY
def search(collection, query):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results


if __name__ == "__main__":
    pages = extract_text(PDF_PATH)
    chunks = chunk_pages(pages)
    collection = store_embeddings(chunks)

    results = search(collection, "refund policy")

    print("\n--- SEARCH RESULT ---\n")
    print(results["documents"][0])
    print(results["metadatas"][0])
