from fastapi import APIRouter, HTTPException
from app.services.ocr.gemini_ocr import run_gemini_ocr
from app.services.ocr.dots_ocr import run_dots_ocr

router = APIRouter()


@router.post("/gemini")
async def gemini_ocr(file_url: str):
    text = await run_gemini_ocr(file_url)
    if not text:
        raise HTTPException(status_code=500, detail="Gemini OCR failed")
    return {"engine": "gemini", "text": text}


@router.post("/dotocr")
async def dotocr(file_url: str):
    text = await run_dots_ocr(file_url)
    if not text:
        raise HTTPException(status_code=500, detail="DotOCR failed")
    return {"engine": "dotocr", "text": text}
