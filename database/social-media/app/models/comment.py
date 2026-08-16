from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base, TimestampMixin


class Comment(Base, TimestampMixin):
    __tablename__ = "comments"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    text: Mapped[str] = mapped_column(String(255))
    

