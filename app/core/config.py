from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "FAQs RAG API"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # Vertex AI Settings
    GOOGLE_CLOUD_PROJECT: str | None = None
    GOOGLE_CLOUD_LOCATION: str = "us-central1"
    GOOGLE_API_KEY: str | None = None
    
    # RAG Settings (to be filled in .env)
    OPENAI_API_KEY: str | None = None
    LLM_PROVIDER: str = "vertex"  # Can be "vertex" or "openai"
    EMBEDDING_PROVIDER: str = "vertex"  # Can be "vertex" or "openai"
    VECTOR_DB_URL: str = "http://chromadb:8000"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

settings = Settings()
