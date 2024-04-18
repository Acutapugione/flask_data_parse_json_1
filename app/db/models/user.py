from typing import List
from .. import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = "users"

    nickname: Mapped[str] 
    email: Mapped[str]
    password: Mapped[str]

    events: Mapped[List["Event"]] = relationship(back_populates="user")

    def is_active(self)->bool:
        return True
    def is_authenticated(self)->bool:
        return True
    def is_anonymous(self)->bool:
        return False
    def get_id(self)->str:
        return f"{self.id}"