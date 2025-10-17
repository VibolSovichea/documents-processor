from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile


class UploadRequest(BaseModel):
    files: Optional[list[UploadFile]] = None
    file_urls: Optional[list[str]] = None
