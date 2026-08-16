from sqlalchemy import ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.mixin import TimestampMixin


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User

class Follow(Base, TimestampMixin):
    __tablename__ = "follows"
    
    __table_args__ = (
        UniqueConstraint("follower_id", "following_id"),
        CheckConstraint("follower_id != following_id")
    )
    
    id: Mapped[int] = mapped_column(primary_key=True)
    follower_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    following_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    
    follower: Mapped["User"] = relationship(foreign_keys=[follower_id],back_populates="following")
    following: Mapped["User"] = relationship(foreign_keys=[following_id], back_populates="followers")
    