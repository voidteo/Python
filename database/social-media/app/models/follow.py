from sqlalchemy import ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base, TimestampMixin


class Follow(Base, TimestampMixin):
    __tablename__ = "follows"
    
    __table_args__ = (
        UniqueConstraint("follower_id", "following_id"),
        CheckConstraint("follower_id != following_id")
    )
    
    id: Mapped[int] = mapped_column(primary_key=True)
    follower_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    following_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    