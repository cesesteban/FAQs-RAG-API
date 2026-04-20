from pydantic import BaseModel, Field
from typing import List, Optional

class RAGQuery(BaseModel):
    query: str
    top_k: int = 3
    lang: str = "es"

class AuditStep(BaseModel):
    iteration: int
    feedback: str
    approved: bool

class TokenTelemetry(BaseModel):
    coordination_tokens: int = 0
    resolution_tokens: int = 0
    audit_tokens: int = 0
    total_tokens: int = 0

class RAGResponse(BaseModel):
    user_question: str = Field(..., description="The original query from the user")
    system_answer: str = Field(..., description="The final generated response")
    chunks_related: List[str] = Field(..., description="Fragments utilized for generation")
    context_hash: str
    audit_trace: List[AuditStep]
    attempts: int
    latency_ms: float
    telemetry: TokenTelemetry
    why_it_works: str
    evaluation: Optional[dict] = None
