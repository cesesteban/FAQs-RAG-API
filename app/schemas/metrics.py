from pydantic import BaseModel
from typing import List, Optional

class MetricsSummary(BaseModel):
    total_interactions: int
    avg_latency_ms: float
    total_tokens_consumed: int
    avg_score: float
    language_distribution: dict

class HistoryResponse(BaseModel):
    summary: MetricsSummary
    history: List[dict]
