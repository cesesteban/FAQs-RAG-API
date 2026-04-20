from fastapi import APIRouter
from app.api.v1.endpoints import faq, rag, metrics

api_router = APIRouter()

api_router.include_router(faq.router, prefix="/faqs", tags=["FAQs"])
api_router.include_router(rag.router, prefix="/rag", tags=["RAG"])
api_router.include_router(metrics.router, prefix="/metrics", tags=["Architecture Metrics"])
