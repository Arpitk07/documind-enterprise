import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import QueryRequest, QueryResponse
from backend.rag import rag_system

# Load environment variables
load_dotenv()

# Configuration from environment
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))

# Initialize FastAPI app
app = FastAPI(
    title="DocuMind Enterprise API",
    description="Document-grounded question answering system",
    version="1.0.0"
)

# Add CORS middleware for potential frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "OK"}


@app.post("/query", response_model=QueryResponse)
async def query_documents(request: QueryRequest):
    """
    Query the document database with a question.
    
    Returns a grounded answer based on the document context,
    or explicitly states when information is not available.
    """
    try:
        # Validate input
        if not request.question or not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        # Run RAG pipeline
        answer = rag_system.query(request.question)
        
        return QueryResponse(answer=answer)
    
    except Exception as e:
        # Handle errors gracefully
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "DocuMind Enterprise API",
        "docs": "/docs",
        "health": "/health",
        "query": "/query"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=API_HOST, port=API_PORT, reload=True)
