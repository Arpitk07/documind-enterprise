from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    question: str
    top_k: int = 3


class Source(BaseModel):
    page: Optional[int]
    document: Optional[str]
    content: Optional[str]


class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]


class StreamChunk(BaseModel):
    token: str
    is_last: bool