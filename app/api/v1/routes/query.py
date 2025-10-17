from fastapi import APIRouter, HTTPException
from app.schemas.query import QueryRequest
from app.services.query_service import query_context

router = APIRouter()


@router.post("/")
async def query_documents(request: QueryRequest):
    response = await query_context(request.prompt)
    if not response:
        raise HTTPException(status_code=404, detail="No relevant context found.")
    return {"context": response}
