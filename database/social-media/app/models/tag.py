from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.mixin import TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.post_tag import PostTag
    from app.models.tag import Tag

class Tag(Base, TimestampMixin):
    __tablename__ = "tags"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(500), nullable=True, unique=True)
    

    post_tags: Mapped[list["PostTag"]] = relationship(back_populates="tag")
    
    posts: Mapped[list["Tag"]] = relationship(secondary="post_tags", back_populates="tags")
    