from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base, TimestampMixin



class User(Base, TimestampMixin):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    bio: Mapped[str] = mapped_column(String(250), nullable=True)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    

    