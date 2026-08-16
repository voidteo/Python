from sqlalchemy import String, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base, TimestampMixin


class Post(Base, TimestampMixin):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(default=False)
    
    