from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLoacal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLoacal()
    try:
        yield db
    finally:
        db.close()
