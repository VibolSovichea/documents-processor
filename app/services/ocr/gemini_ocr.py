import os
import base64
import aiohttp
from app.core.config import settings


async def run_gemini_ocr(file_path: str) -> str | None:
    try:
        with open(file_path, "rb") as f:
            content = f.read()
    except FileNotFoundError:
        return None

    b64 = base64.b64encode(content).decode("utf-8")
    mime_type = "image/png"

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "inlineData": {
                            "mimeType": mime_type,
                            "data": b64,
                        }
                    },
                    {"text": "Extract all text from the image in Khmer and English"},
                ]
            }
        ],
        "config": {"temperature": 0.1},  # lower temperature for OCR task
    }

    endpoint = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"
    url = f"{endpoint}?key={settings.GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as resp:
            if resp.status != 200:
                print(f"API Error: Status {resp.status}, Response: {await resp.text()}")
                return None

            result = await resp.json()

    text = None
    try:
        text = result["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError):
        print("Error: Could not find extracted text in the API response.")
        # print(f"Full response: {result}")
        return None

    return text
