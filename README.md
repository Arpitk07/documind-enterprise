**Week 1 – Document Ingestion & Vectorization
🔍 Project Overview**

DocuMind Enterprise is a Retrieval-Augmented Generation (RAG) based system designed to answer questions strictly from internal documents such as SOPs, policies, and manuals.

Week 1 focuses on building a strong foundation by converting PDF documents into semantically searchable vector embeddings. No chatbot or API is implemented yet — correctness of data ingestion is the priority.

**🎯 Week 1 Objective**

_The goal of Week 1 is to ensure that:_

PDF documents can be reliably loaded

Text is extracted cleanly

Content is split into meaningful chunks

Chunks are converted into vector embeddings

Semantic similarity search works correctly

A stable ingestion pipeline is critical before introducing LLM-based generation.


**🧠 Architecture (Week 1 Scope)**

PDF Document
     ↓
Text Extraction (PyMuPDF)
     ↓
Chunking (Recursive Character Splitter)
     ↓
Embeddings (Sentence Transformers)
     ↓
Vector Storage (ChromaDB)
     ↓
Semantic Search (Similarity Query)

**🛠️ Tech Stack (Week 1)**
Component	Tool / Library
Language	Python 3
PDF Parsing	PyMuPDF
Text Chunking	langchain-text-splitters
Embeddings	all-MiniLM-L6-v2 (SentenceTransformers)
Vector Database	ChromaDB (local)

**Project Structure:**
documind/
│
├── ingestion/
│   └── ingest.py          # PDF ingestion & vectorization logic
│
├── data/
│   └── pdfs/
│       └── sample.pdf     # Input document
│
├── requirements.txt
├── .gitignore

Environment	Python venv

**🚀 Next Steps (Week 2 Preview)**

In Week 2, the project will be extended to:

Integrate a local LLM (Ollama)

Implement RAG-based answer generation

Enforce hallucination-safe responses

Answer questions strictly from document content

**👤 Team

Team Lead: Arpit

Intern A (Backend): Janhavi

Intern B (Data / QA): Mathangi**
