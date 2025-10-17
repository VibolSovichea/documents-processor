from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from app.services.vectorstore import get_pinecone_client
from app.core.config import settings


async def embed_and_store(text: str):
    embeddings = OpenAIEmbeddings(
        model=settings.EMBEDDING_MODEL, openai_api_key=settings.OPENAI_API_KEY
    )
    pinecone = get_pinecone_client()
    index = pinecone.Index(settings.PINECONE_INDEX)
    vectorstore = PineconeVectorStore(index=index, embedding=embeddings)
    vectorstore.add_texts([text])
