import aiohttp
from app.core.config import settings


async def run_dots_ocr(file_path: str) -> str | None:
    # Read binary file
    with open(file_path, "rb") as f:
        content = f.read()

    files = {"file": (file_path, content)}
    data = {
        # any parameters required by DotOCR (language, etc.)
        "lang": "km,en"
    }
    headers = {"Authorization": f"Bearer {settings.DOTS_OCR_API_KEY}"}

    url = "https://api.dots.ocr/v1/ocr"  # replace with actual DotOCR endpoint

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data, files=files) as resp:
            if resp.status != 200:
                return None
            result = await resp.json()

    # Parse result — depends on DotOCR response format
    # Suppose the JSON is: { "text": "...extracted text..." }
    text = result.get("text")
    return text
