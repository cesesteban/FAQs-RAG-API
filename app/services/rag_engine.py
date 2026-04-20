import time
import hashlib
from fastapi import HTTPException
from app.schemas.rag import RAGQuery, RAGResponse, AuditStep, TokenTelemetry
from app.core.config import settings
from app.services.graph_workflow import create_rag_graph, RAGState
from app.services.context_engineering import estimate_tokens
from app.core.i18n import get_translation
from app.services.history_service import save_interaction

# Initialize the graph once
rag_app = create_rag_graph()

async def generate_rag_response(payload: RAGQuery) -> RAGResponse:
    """
    Workflow using LangGraph with Safety, Retrieval, CoT Generation, and Evaluation.
    """
    start_time = time.time()
    
    # Initial state
    initial_state: RAGState = {
        "query": payload.query,
        "context": [],
        "analysis": "",
        "strategy": "",
        "risks": "",
        "answer": "",
        "is_safe": True,
        "safety_reason": "",
        "score": 0.0,
        "evaluation_reason": "",
        "iterations": 1,
        "next_step": "",
        "lang": payload.lang
    }
    
    # Execute Graph
    try:
        final_state = rag_app.invoke(initial_state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Graph execution failed: {str(e)}")

    if not final_state.get("is_safe"):
        raise HTTPException(
            status_code=400, 
            detail=get_translation(payload.lang, "safety_blocked", reason=final_state.get("safety_reason"))
        )

    context_hash = hashlib.sha256(payload.query.encode()).hexdigest()
    latency = (time.time() - start_time) * 1000
    
    # Telemetry estimation
    coord_tokens = estimate_tokens(payload.query) + 200
    resolution_tokens = estimate_tokens(" ".join(final_state.get("context", []))) + 500
    
    response_data = RAGResponse(
        user_question=payload.query,
        system_answer=final_state.get("answer", ""),
        chunks_related=final_state.get("context", []),
        context_hash=context_hash,
        audit_trace=[
            AuditStep(iteration=1, feedback="Graph Flow Completed", approved=True)
        ],
        attempts=1,
        latency_ms=round(latency, 2),
        telemetry=TokenTelemetry(
            coordination_tokens=coord_tokens,
            resolution_tokens=resolution_tokens,
            audit_tokens=150,
            total_tokens=coord_tokens + resolution_tokens + 150
        ),
        why_it_works=get_translation(payload.lang, "why_it_works"),
        evaluation={
            "score": final_state.get("score"),
            "reason": final_state.get("evaluation_reason")
        }
    )
    
    # Persistir interacción con metadatos extra (como idioma)
    interaction_to_save = response_data.model_dump()
    interaction_to_save["lang"] = payload.lang
    
    # En un entorno async real, podríamos lanzar esto como una background task
    import asyncio
    asyncio.create_task(save_interaction(interaction_to_save)) 
    
    return response_data
