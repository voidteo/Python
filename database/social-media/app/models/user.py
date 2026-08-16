from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.mixin import TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.post import Post
    from app.models.comment import Comment
    from app.models.like import Like
    from app.models.follow import Follow

class User(Base, TimestampMixin):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    bio: Mapped[str] = mapped_column(String(250), nullable=True)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    comments: Mapped[list["Comment"]] = relationship(back_populates="user")
    likes: Mapped[list["Like"]] = relationship(back_populates="user")
    
    following: Mapped[list["Follow"]] = relationship(foreign_keys="Follow.follower_id", back_populates="follower")
    followers: Mapped[list["Follow"]] = relationship(foreign_keys="Follow.following_id", back_populates="following")
    
    