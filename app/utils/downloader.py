import aiohttp
import tempfile
import os
from fastapi import UploadFile


async def fetch_file(
    files: list[UploadFile] | None, urls: list[str] | None
) -> list[str]:
    paths = []
    tmpdir = tempfile.gettempdir()

    # Save uploaded files
    if files:
        for f in files:
            path = os.path.join(tmpdir, f.filename)
            with open(path, "wb") as buffer:
                buffer.write(await f.read())
            paths.append(path)

    # Download remote URLs
    if urls:
        async with aiohttp.ClientSession() as session:
            for url in urls:
                name = url.split("/")[-1]
                path = os.path.join(tmpdir, name)
                async with session.get(url) as resp:
                    if resp.status == 200:
                        with open(path, "wb") as f:
                            f.write(await resp.read())
                        paths.append(path)

    return paths
