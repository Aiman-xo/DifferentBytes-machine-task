from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine

from app.core.config import DB_URL

engine = create_engine(DB_URL)

sessionLocal = sessionmaker(
    autoflush=True,
    bind=engine,
    autocommit = False
)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()