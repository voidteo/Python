from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase, sessionmaker


DB_URL = "postgresql+psycopg2://postgres:teopostgres@localhost:5432/testor_db"

engine = create_engine(DB_URL, echo=True)

class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)

