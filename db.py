from sqlalchemy import create_engine, Column, String, LargeBinary, Text
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Define table for storing documents and embeddings
class Document(Base):
    __tablename__ = "documents"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    embedding = Column(LargeBinary, nullable=False)

def init_db():
    """Create database tables."""
    Base.metadata.create_all(bind=engine)
