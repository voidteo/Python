from sqlalchemy import create_engine, ForeignKey, String, Boolean, select, Table, Column, func

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session, selectinload, aliased

DB_URL = "postgresql+psycopg2://postgres:teopostgres@localhost:5432/test_db"

engine = create_engine(DB_URL, echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique = True)
    is_active: Mapped[bool] = mapped_column(default=True)
    
    
    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    
class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(250))
    is_active: Mapped[bool] = mapped_column(default=True)
    
    
    user: Mapped["User"] = relationship(back_populates= "posts")
    
Base.metadata.create_all(engine)


user = User(
    name= "Teo",
    email= "teo7@gmail.com",
)

post = Post(
    title = "Rise from darkness"
)

user.posts.append(post)
#post.user = user

session = Session(engine)

session.add(user)

session.flush()

print(User.posts)