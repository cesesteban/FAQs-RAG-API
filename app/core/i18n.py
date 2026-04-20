translations = {
    "en": {
        "welcome": "Welcome to the FAQ RAG API",
        "safety_blocked": "Safety Layer Blocked Request: {reason}",
        "graph_failed": "Graph execution failed: {reason}",
        "system_answer": "System Answer",
        "why_it_works": "LangGraph Multi-Agent Flow: Safety -> Retrieval -> CoT Generator -> Evaluator."
    },
    "es": {
        "welcome": "Bienvenido a la API FAQ RAG",
        "safety_blocked": "Capa de Seguridad bloqueó la solicitud: {reason}",
        "graph_failed": "Error en la ejecución del grafo: {reason}",
        "system_answer": "Respuesta del Sistema",
        "why_it_works": "Flujo Multi-Agente con LangGraph: Seguridad -> Recuperación -> Generador CoT -> Evaluador."
    }
}

def get_translation(lang: str, key: str, **kwargs):
    text = translations.get(lang, translations["en"]).get(key, translations["en"][key])
    return text.format(**kwargs)
