import os
import pathlib
import uuid

from fastapi import UploadFile

FILE_ROOT = "files"


async def save_file(image: UploadFile) -> str:
    file_name = f"{str(uuid.uuid4())}_{image.filename}"
    p = pathlib.Path(FILE_ROOT)
    p.mkdir(exist_ok=True)
    file_path = os.path.join(str(p), file_name)
    with open(file_path, "wb") as f:
        content = await image.read()
        f.write(content)
    return file_name


def exist(image_path: str) -> bool:
    p = pathlib.Path(os.path.join(FILE_ROOT, image_path))
    return p.exists()


def remove_file(image_path: str) -> None:
    file_path = os.path.join(FILE_ROOT, image_path)
    os.remove(file_path)
