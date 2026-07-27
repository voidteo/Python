from datetime import datetime, timezone, UTC

from sqlalchemy import create_engine, String, ForeignKey, DateTime, Boolean, select

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

DB_URL = "postgresql+psycopg2://postgres:teopostgres@localhost:5432/test_db"

engine = create_engine(DB_URL, echo=True)



class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    
    
    posts: Mapped[list["Post"]] = relationship(back_populates= "user")
    

class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(String(255))
    is_published: Mapped[bool] = mapped_column( default=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    
    
    user: Mapped["User"] = relationship(back_populates= "posts")
    

Base.metadata.create_all(engine)

session = Session(engine)


"""user = User(
    name = "Teo",
    email = "voidteo@gmail.com",
    password = "qwerty!@#",
    created_at = datetime.now(UTC)
)

user1 = User(
    name = "Ciara",
    email = "ciara14@gmail.com",
    password = "ciara1999",
    created_at = datetime.now(UTC)
)


session.add(user)
session.add(user1)

session.flush()
session.commit()


user3 = User(
    name = "Alex",
    email= "Mahone@gmail.com",
    password= "prison123",
    created_at= datetime.now(UTC)
)

session.add(user3)
session.commit()"""

user =  User(
    name= "Balto",
    email = "balto@gmail.com",
    password = "baltoice12",
    created_at = datetime.now(UTC)   
)

post = Post(
    user_id = 4,
    title = "Balto's adventure",
    content = "Balto joined in logistics with dogs"
)

print(user.posts)
print(post.user)

print("-" * 30)

user.posts.append(post)

print(user.posts)
print(post.user)