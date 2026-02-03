import os
import fitz  # PyMuPDF
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "..", "data", "pdfs", "hr_policy.py.pdf")
CHROMA_DIR = os.path.join(BASE_DIR, "..", "chroma_db")

# -----------------------------
# Extract text
# -----------------------------
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

# -----------------------------
# Chunk text
# -----------------------------
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
                    "source": "hr_policy.py.pdf"
                }
            })

    return chunks

# -----------------------------
# Store embeddings in Chroma
# -----------------------------
def store_embeddings(chunks):
    # Create a persistent Chroma client
    client = chromadb.Client(Settings(persist_directory=CHROMA_DIR))
    
    # Get or create the collection
    collection = client.get_or_create_collection(name="documind")

    # Load the SentenceTransformer model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Add embeddings for each chunk
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk["text"]).tolist()
        collection.add(
            ids=[str(i)],
            documents=[chunk["text"]],
            metadatas=[chunk["metadata"]],
            embeddings=[embedding]
        )

    # Save/persist the database

    return collection

# -----------------------------
# Search embeddings
# -----------------------------
def search(collection, query):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    return results

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    print(" Extracting text...")
    pages = extract_text(PDF_PATH)

    print(" Chunking pages...")
    chunks = chunk_pages(pages)

    print(" Creating embeddings...")
    collection = store_embeddings(chunks)

    print(" Testing search...")
    results = search(collection, "refund policy")

    print("\n--- SEARCH RESULT ---\n")
    print(results["documents"][0])
    print(results["metadatas"][0])

    print("\n Ingestion completed successfully!")
