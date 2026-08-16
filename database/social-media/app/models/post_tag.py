from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class PostTag(Base):
    __tablename__ = "post_tags"
    
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), primary_key=True)
    
    
    