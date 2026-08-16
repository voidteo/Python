from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base, TimestampMixin


class Tag(Base, TimestampMixin):
    __tablename__ = "tags"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(500), nullable=True, unique=True)
    

