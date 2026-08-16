from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql+psycopg2://postgres:teopostgres@localhost:5432/social_db"


engine = create_engine(DB_URL, echo=True)


SessionLocal = sessionmaker(bind= engine, expire_on_commit=False, autoflush=False)

