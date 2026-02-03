from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from typing import Generator
import time

from api.schemas import (
    ChatRequest,
    ChatResponse,
    StreamChunk,
    Source
)

from retrieval.query import (
    get_rag_response,
    get_rag_response_stream
)

app = FastAPI(
    title="DocuMind Enterprise API",
    description="RAG-based Enterprise Knowledge Assistant",
    version="1.0.0"
)

# ---------------------------------
# Health Check
# ---------------------------------
@app.get("/")
def health():
    return {"status": "DocuMind API is running 🚀"}

# ---------------------------------
# Chat Endpoint (Non-streaming)
# ---------------------------------
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # ⚡ FAST PATCH: avoid calling get_rag_response
    answer = f"Simulated answer for: {request.question}"

    return ChatResponse(
        answer=answer,
        sources=[]
    )



# ---------------------------------
# Streaming Chat Endpoint
# ---------------------------------
@app.post("/chat/stream")
def chat_stream(request: ChatRequest):

    def event_generator() -> Generator[str, None, None]:
        for token in get_rag_response_stream(
            request.question,
            request.top_k
        ):
            chunk = StreamChunk(token=token, is_last=False)
            yield chunk.json() + "\n"
            time.sleep(0.02)

        yield StreamChunk(token="", is_last=True).json()

    return StreamingResponse(
        event_generator(),
        media_type="application/json"
    )
