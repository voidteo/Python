from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base, TimestampMixin


class Like(Base, TimestampMixin):
    __tablename__ = "likes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    

