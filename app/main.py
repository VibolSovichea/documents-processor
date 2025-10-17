from fastapi import FastAPI
from app.api.v1.routes import upload, ocr, query
from app.core.config import settings
import uvicorn

app = FastAPI(
    title="Document Processor API",
    version="1.0.0",
    description="OCR + Embedding + Vector Search microservice",
)

app.include_router(upload.router, prefix="/api/v1/upload", tags=["Upload"])
app.include_router(ocr.router, prefix="/api/v1/ocr", tags=["OCR"])
app.include_router(query.router, prefix="/api/v1/query", tags=["Query"])


@app.get("/health")
def health_check():
    return {"status": "ok", "env": settings.ENV}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
