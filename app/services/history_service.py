import json
import os
from datetime import datetime
from typing import List
from app.schemas.rag import RAGResponse

METRICS_FILE = "app/data/history_metrics.json"

async def save_interaction(interaction_data: dict):
    """
    Guarda la interacción en un archivo JSON para el historial y métricas.
    """
    # Asegurar que el directorio existe
    os.makedirs(os.path.dirname(METRICS_FILE), exist_ok=True)
    
    # Agregar timestamp
    interaction_data["timestamp"] = datetime.now().isoformat()
    
    # Leer historial existente
    history = []
    if os.path.exists(METRICS_FILE):
        try:
            with open(METRICS_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except json.JSONDecodeError:
            history = []
            
    # Agregar nueva entrada
    history.append(interaction_data)
    
    # Guardar de nuevo (en un sistema real usaríamos una DB async)
    with open(METRICS_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)
        
    # Generar salidas extrictas de ejemplo en outputs/sample_queries.json
    OUTPUTS_DIR = "outputs"
    SAMPLE_FILE = os.path.join(OUTPUTS_DIR, "sample_queries.json")
    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    
    samples = []
    if os.path.exists(SAMPLE_FILE):
        try:
            with open(SAMPLE_FILE, "r", encoding="utf-8") as f:
                samples = json.load(f)
        except json.JSONDecodeError:
            samples = []
            
    if len(samples) < 3:
        sample_entry = {
            "user_question": interaction_data.get("user_question", ""),
            "system_answer": interaction_data.get("system_answer", ""),
            "chunks_related": interaction_data.get("chunks_related", [])
        }
        samples.append(sample_entry)
        with open(SAMPLE_FILE, "w", encoding="utf-8") as f:
            json.dump(samples, f, indent=4, ensure_ascii=False)

async def get_history_metrics() -> List[dict]:
    """
    Retorna todo el historial de métricas.
    """
    if not os.path.exists(METRICS_FILE):
        return []
        
    with open(METRICS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
