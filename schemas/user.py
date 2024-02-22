from typing import Literal, Annotated, Union

from fastapi import UploadFile, Form, File
from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    phone: str
    mobile_os: Literal["ios", "android"]


class UserCreate(UserBase):
    image: Union[UploadFile, None] = Field(File(...), exclude=True)

    @classmethod
    def from_formdata(
        cls,
        *,
        name: Annotated[str, Form(...)],
        phone: Annotated[str, Form(...)],
        mobile_os: Annotated[str, Form(...)],
        image: UploadFile # | None = None
    ):
        return cls(name=name, phone=phone, mobile_os=mobile_os, image=image)


class UserSchema(UserBase):
    image_path: str
