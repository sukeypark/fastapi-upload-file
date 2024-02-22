import sqlalchemy.orm as so
from sqlalchemy import String

from db import Base


class User(Base):
    __tablename__ = "user"

    name: so.Mapped[str] = so.mapped_column("name", String(), primary_key=True)
    phone: so.Mapped[str] = so.mapped_column("phone", String())
    image_path: so.Mapped[str] = so.mapped_column("image_path", String())
    mobile_os: so.Mapped[str] = so.mapped_column("mobile_os", String())
