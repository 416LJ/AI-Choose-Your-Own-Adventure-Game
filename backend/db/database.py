from sqlalchemy import create_engine # wraps are DB we are interacting with
from sqlalchemy.orm import sessionmaker # creates session for us to interact with db
from sqlalchemy.ext.declarative import declarative_base

from core.config import settings

# create db engine and connect to url
engine = create_engine(
    settings.DATABASE_URL
)

# create session and bind to engine created above
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():

    db = SessionLocal()

    try:
        # YIELD Pauses Execution: Unlike return, which terminates a function completely, yield pauses the function's execution and saves its local state (variables, position in code, etc.).
        yield db

    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)

