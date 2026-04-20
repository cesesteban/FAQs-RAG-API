from fastapi import APIRouter
from app.services.history_service import get_history_metrics
from app.schemas.metrics import HistoryResponse, MetricsSummary

router = APIRouter()

@router.get("/report", response_model=HistoryResponse)
async def get_metrics_report() -> HistoryResponse:
    """
    Genera un reporte resumido de métricas de arquitectura y el historial completo.
    """
    history = await get_history_metrics()
    
    if not history:
        summary = MetricsSummary(
            total_interactions=0,
            avg_latency_ms=0.0,
            total_tokens_consumed=0,
            avg_score=0.0,
            language_distribution={}
        )
        return HistoryResponse(summary=summary, history=[])
    
    # Calcular resumen
    total = len(history)
    sum_latency = sum(item.get("latency_ms", 0) for item in history)
    sum_tokens = sum(item.get("telemetry", {}).get("total_tokens", 0) for item in history)
    
    # Calcular promedio de score (solo si la evaluación existe y tiene score)
    scores = [item.get("evaluation", {}).get("score", 0) for item in history if item.get("evaluation")]
    avg_score = sum(scores) / len(scores) if scores else 0.0
    
    # Distribución de idiomas (asumiendo que guardamos el lang o lo inferimos)
    # Nota: RAGResponse no tiene 'lang' directamente, pero podemos inferirlo de query_cli o mandarlo en el payload
    # Por ahora usaremos un placeholder o lo buscaremos en el historial si lo agregamos
    langs = {}
    for item in history:
        # Intentamos obtener idioma si lo guardamos (necesitamos actualizar save_interaction para incluirlo)
        l = item.get("lang", "unknown")
        langs[l] = langs.get(l, 0) + 1

    summary = MetricsSummary(
        total_interactions=total,
        avg_latency_ms=round(sum_latency / total, 2),
        total_tokens_consumed=sum_tokens,
        avg_score=round(avg_score, 2),
        language_distribution=langs
    )
    
    return HistoryResponse(summary=summary, history=history)
