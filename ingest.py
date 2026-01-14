import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Path where PDFs are stored
PDF_FOLDER = "data/pdfs"

# Load all PDFs
documents = []
for file in os.listdir(PDF_FOLDER):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(PDF_FOLDER, file))
        documents.extend(loader.load())

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

# Create embeddings and store in ChromaDB
db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    persist_directory="chroma_db"
)

db.persist()

print("✅ PDFs successfully ingested into ChromaDB")
print(f"Total chunks stored: {len(chunks)}")