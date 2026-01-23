DocuMind Enterprise
Weeks 1 & 2 Progress Report
---
Project Overview

DocuMind Enterprise is an AI-powered document intelligence system designed to ingest PDF documents, generate embeddings, store them in a vector database, and enable accurate question-answering using Retrieval-Augmented Generation (RAG). The system focuses on enterprise-level SOPs, policies, and internal documentation.

Objectives

Primary Objectives

Build a scalable document ingestion pipeline

Extract text from PDFs reliably

Generate embeddings using LLM-based embedding models

Store embeddings in a vector database for semantic search

Enable question-answering strictly from provided documents

Learning Objectives

Understand vector databases and embeddings

Gain hands-on experience with LangChain and ChromaDB

Learn Git and GitHub workflow for project version control

Build a foundation for enterprise-grade AI assistants

Week 1 Progress

Goals Achieved

Project structure initialization

Environment setup using Python virtual environment

Installed and configured required dependencies

Implemented PDF text extraction using PyMuPDF (fitz)

Built initial ingestion pipeline

Generated and stored embeddings successfully

Verified vector storage (42 embeddings stored)


Key Technologies Used

Python 3.x

PyMuPDF (PDF text extraction)

LangChain

Ollama (LLM & Embeddings)

ChromaDB (Vector Database)


Folder Structure (Initial)

documind/
│── ingestion/
│   └── ingest.py
│── data/
│   └── pdfs/
│── vectordb/
│── requirements.txt
│── .gitignore

Outcomes

Successfully converted PDFs into embeddings

Validated document ingestion flow

Understood limitations of scanned vs text-based PDFs 

Week 2 Progress

Goals Achieved

Integrated retrieval-based question answering

Implemented RetrievalQA chain

Designed custom prompt template for enterprise SOP assistant

Restricted responses strictly to document context

Initialized Git repository and pushed project to GitHub

Resolved GitHub authentication and remote issues

Improved .gitignore to exclude venv and vectordb


Functional Enhancements

Context-aware question answering

Error handling for missing PDFs

Clean separation between ingestion and retrieval logic


Sample Prompt Behavior

Answers only from documents

Returns fallback response when information is unavailable

Team Contribution

Arpit (Primary Contributor)

Designed overall project architecture

Implemented ingestion and embedding pipeline

Integrated ChromaDB and LangChain

Managed GitHub repository and version control

Debugged environment, path, and permission issues

Team Support & Guidance

Conceptual discussions on RAG pipeline

Debugging assistance and architectural suggestions

Documentation and workflow optimization

Challenges Faced

Handling incorrect PDF paths

Differentiating scanned vs text-based PDFs

GitHub permission and remote URL conflicts

Managing large folders like venv and vectordb
Future Progress Plan

Short-Term (Week 3–4)

Add support for multiple PDFs ingestion

Improve chunking strategy

Enhance metadata storage

Implement source citation in answers


Mid-Term

Add web-based UI (Streamlit / React)

Role-based access for enterprise users

Improve retrieval accuracy using reranking


Long-Term

Support additional document formats (DOCX, PPTX)

Multi-user authentication

Deployment on cloud infrastructure

Enterprise-ready logging and monitoring
