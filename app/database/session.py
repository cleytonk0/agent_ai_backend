from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Carrega variáveis de ambiente
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "agent_db")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL) #cria a conexão com o banco de dados
# cria a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)