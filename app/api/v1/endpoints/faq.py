from fastapi import APIRouter, HTTPException
from app.schemas.faq import FAQRead, FAQCreate
from app.services.history_service import get_history_metrics

router = APIRouter()

@router.get("/", response_model=list[FAQRead])
async def list_faqs() -> list[dict]:
    """List all available FAQs based on real interaction history."""
    metrics = await get_history_metrics()
    
    if not metrics:
        return []
        
    seen = set()
    faqs = []
    
    for item in metrics:
        question = item.get("user_question", "")
        if not question or question in seen:
            continue
            
        seen.add(question)
        faqs.append({
            "id": len(faqs) + 1,
            "question": question,
            "answer": item.get("system_answer", "")
        })
        
    return faqs

@router.post("/", response_model=FAQRead, status_code=201)
async def create_faq(payload: FAQCreate) -> dict:
    """Create a new FAQ entry."""
    raise HTTPException(status_code=501, detail="Manual FAQ creation is disabled. FAQs are generated from real interactions.")
