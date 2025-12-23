from sqlalchemy import Column, Integer, Text, DateTime # importa os tipos de dados do SQLAlchemy
from datetime import datetime # importa a classe datetime para lidar com datas e horas
from datetime import datetime, timezone # importa timezone para lidar com fusos horários
from app.database.base import Base

class Conversation(Base):
    __tablename__ = "conversations" # define o nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True) # define a coluna 'id' como chave primária
    user_input = Column(Text, nullable=False) # define a coluna 'user_input' para armazenar a entrada do usuário
    agent_response = Column(Text, nullable=False) # define a coluna 'agent_response' para armazenar a resposta do agente
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)) # define a coluna 'created_at' para armazenar a data e hora de criação, com fuso horário UTC