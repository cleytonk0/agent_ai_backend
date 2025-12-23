from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/agent_db"

engine = create_engine(DATABASE_URL) #cria a conexão com o banco de dados
# cria a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)