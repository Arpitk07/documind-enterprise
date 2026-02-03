import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA




BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DB_PATH = os.path.join(BASE_DIR, "..", "chroma_db")

def get_rag_response(question: str, top_k: int = 3):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
def get_rag_response_stream(question: str, top_k: int = 3):
    """
    Simple streaming: generate full answer,
    then yield it token-by-token (Week 3 compliant).
    """
    answer, sources = get_rag_response(question, top_k)

    for token in answer.split():
        yield token + " "


    db = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )

    retriever = db.as_retriever(search_kwargs={"k": top_k})

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a corporate SOP assistant.
Answer ONLY from the provided context.
If not found, say: "I don't know."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    llm = Ollama(model="llama2")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    result = qa(question)

    sources = []
    for doc in result["source_documents"]:
        sources.append({
            "page": doc.metadata.get("page", 0),
            "document": doc.metadata.get("source", "unknown"),
            "content": doc.page_content[:200]
        })
    print("DEBUG: returning from get_rag_response")

    return result["result"], sources