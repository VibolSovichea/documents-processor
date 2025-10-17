from app.services.ocr.gemini_ocr import run_gemini_ocr
from app.services.ocr.dots_ocr import run_dots_ocr
from app.services.embeddings import embed_and_store
from app.utils.downloader import fetch_file
from app.schemas.upload import UploadRequest


async def process_documents(req: UploadRequest):
    """
    Handles: file download → OCR → embeddings → store in Pinecone.
    """
    texts = []

    # Download or read files
    file_paths = await fetch_file(req.files, req.file_urls)

    for path in file_paths:
        try:
            # Try Gemini first, fallback to DotOCR
            text = await run_gemini_ocr(path) or await run_dots_ocr(path)
            if text:
                await embed_and_store(text)
                texts.append({"file": path, "status": "processed"})
            else:
                texts.append({"file": path, "status": "failed"})
        except Exception as e:
            texts.append({"file": path, "error": str(e)})

    return texts
