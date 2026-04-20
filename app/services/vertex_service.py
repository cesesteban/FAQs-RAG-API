from typing import Optional
from langchain_google_vertexai import ChatVertexAI, VertexAIEmbeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from app.core.config import settings

def get_llm(model_name: str = "gemini-2.5-flash") -> Optional[any]:
    """
    Returns a configured LLM instance based on .env provider settings.
    """
    if settings.LLM_PROVIDER == "openai":
        return ChatOpenAI(temperature=0.2, model_name="gpt-4o-mini", api_key=settings.OPENAI_API_KEY)

    if not settings.GOOGLE_CLOUD_PROJECT:
        return None
        
    return ChatVertexAI(
        model_name=model_name,
        project=settings.GOOGLE_CLOUD_PROJECT,
        location=settings.GOOGLE_CLOUD_LOCATION,
        temperature=0.2,
        max_output_tokens=1024,
    )

def get_embeddings(model_name: str = "text-embedding-004") -> Optional[any]:
    """
    Returns a configured Embeddings instance based on .env provider settings.
    """
    if settings.EMBEDDING_PROVIDER == "openai":
        return OpenAIEmbeddings(api_key=settings.OPENAI_API_KEY)

    if not settings.GOOGLE_CLOUD_PROJECT:
        return None
        
    return VertexAIEmbeddings(
        model_name=model_name,
        project=settings.GOOGLE_CLOUD_PROJECT,
        location=settings.GOOGLE_CLOUD_LOCATION,
    )
