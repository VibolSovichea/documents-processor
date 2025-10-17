import pinecone
from app.core.config import settings


def get_pinecone_client():
    pinecone.init(
        api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENVIRONMENT
    )
    return pinecone
