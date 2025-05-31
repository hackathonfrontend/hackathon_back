# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres.vbovzftczepcfdxnrzae:IYxl1iu4r9J7vlJT@aws-0-eu-central-1.pooler.supabase.com:6543/postgres?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)