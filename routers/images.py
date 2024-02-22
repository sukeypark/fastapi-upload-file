import os

from fastapi import UploadFile, HTTPException, APIRouter
from fastapi.responses import FileResponse
from starlette import status

from service import image as image_service
from service.image import FILE_ROOT

router = APIRouter()


@router.get("/images/{image_path}", response_class=FileResponse)
async def read_image_data(image_path: str):
    if not image_service.exist(image_path):
        raise HTTPException(status_code=404)
    return os.path.join(FILE_ROOT, image_path)


@router.post("/images")
async def upload_image(image: UploadFile):
    return {"file_path": await image_service.save_file(image)}


@router.delete("/images/{image_path}", status_code=status.HTTP_204_NO_CONTENT)
def remove_image(image_path: str):
    if not image_service.exist(image_path):
        raise HTTPException(status_code=404)
    image_service.remove_file(image_path)
