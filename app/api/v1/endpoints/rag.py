from fastapi import APIRouter
from app.schemas.rag import RAGQuery, RAGResponse
from app.services.rag_engine import generate_rag_response

router = APIRouter()

@router.post("/query", response_model=RAGResponse)
async def perform_rag_query(payload: RAGQuery) -> RAGResponse:
    """
    Perform a RAG query utilizing Vertex AI and an Audit Loop
    as defined in the system architecture.
    """
    return await generate_rag_response(payload)
