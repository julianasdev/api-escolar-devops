# Em seu arquivo database.py (ou onde o engine é criado)
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Pega a URL do banco da variável de ambiente
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./escola.db") 
# O segundo argumento "sqlite:///./escola.db" é um valor padrão 
# caso a variável de ambiente não seja encontrada.

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()