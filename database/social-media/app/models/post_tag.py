from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.post import Post
    from app.models.tag import Tag


class PostTag(Base):
    __tablename__ = "post_tags"
    
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), primary_key=True)
    
    
    post: Mapped["Post"] = relationship(back_populates="post_tags", overlaps="tags")
    tag: Mapped["Tag"] = relationship(back_populates="post_tags", overlaps="posts")
    
    

