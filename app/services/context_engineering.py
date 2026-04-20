from typing import List

def simple_context_reranker(query: str, chunks: List[str]) -> List[str]:
    """
    Implements a simple weight-based reranker or keyword density check
    as mentioned in the M2 technical base (L3).
    """
    # In a real scenario, this could use a Cross-Encoder or a keyword-matching score
    # For now, we simulate sorting by relevance to the query.
    query_terms = set(query.lower().split())
    
    scored_chunks = []
    for chunk in chunks:
        # Simple keyword overlap score
        score = len(query_terms.intersection(set(chunk.lower().split())))
        scored_chunks.append((score, chunk))
        
    # Sort by score descending
    scored_chunks.sort(key=lambda x: x[0], reverse=True)
    
    return [c[1] for c in scored_chunks]

def estimate_tokens(text: str) -> int:
    """
    Simple token estimation (4 chars per token) to meet the 
    observability requirement from the architecture report.
    """
    return len(text) // 4
