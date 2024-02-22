from fastapi import FastAPI

import models
from db import engine
from routers.users import router as user_router
from routers.images import router as image_router

app = FastAPI(title="File Uploader", openapi_url="/openapi.json")
app.include_router(user_router, tags=["users"])
app.include_router(image_router, tags=["images"])


@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)
