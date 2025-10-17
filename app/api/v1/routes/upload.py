from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from typing import Optional
from app.schemas.upload import UploadRequest
from app.services.document_pipeline import process_documents

router = APIRouter()


@router.post("/")
async def upload_documents(
    files: Optional[list[UploadFile]] = None,
    file_urls: Optional[list[str]] = Form(default=None),
):
    if not files and not file_urls:
        raise HTTPException(status_code=400, detail="No files or URLs provided.")

    req = UploadRequest(files=files, file_urls=file_urls)
    result = await process_documents(req)
    return {"status": "success", "processed": result}
