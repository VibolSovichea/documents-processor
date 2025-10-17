from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None
    GEMINI_API_KEY: str | None = None
    DOTS_OCR_API_KEY: str | None = None

    VECTOR_DB: str = "pinecone"
    PINECONE_API_KEY: str | None = None
    PINECONE_ENVIRONMENT: str | None = None
    PINECONE_INDEX: str = "document-index"

    EMBEDDING_MODEL: str = "text-embedding-3-large"
    ENV: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()
