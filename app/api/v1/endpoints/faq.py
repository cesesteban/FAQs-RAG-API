from fastapi import APIRouter, HTTPException
from app.schemas.faq import FAQRead, FAQCreate

router = APIRouter()

# Mock storage for template demonstration
MOCK_FAQS = [
    {"id": 1, "question": "What is life?", "answer": "42"},
]

@router.get("/", response_model=list[FAQRead])
async def list_faqs() -> list[dict]:
    """List all available FAQs."""
    return MOCK_FAQS

@router.post("/", response_model=FAQRead, status_code=201)
async def create_faq(payload: FAQCreate) -> dict:
    """Create a new FAQ entry."""
    new_id = len(MOCK_FAQS) + 1
    new_faq = {"id": new_id, **payload.model_dump()}
    MOCK_FAQS.append(new_faq)
    return new_faq
