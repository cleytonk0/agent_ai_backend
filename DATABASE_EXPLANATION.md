# Explicação do Código Relacionado ao Banco de Dados

Este documento explica todo o código relacionado ao banco de dados no projeto AI Agent Backend.

## 1. Estrutura Geral

O projeto usa **SQLAlchemy** como ORM (Object-Relational Mapping) para interagir com o banco de dados. Atualmente configurado para **MySQL** via PyMySQL.

### Arquivos Principais:

- `app/database/base.py`: Define a base para os modelos.
- `app/database/session.py`: Configura a conexão e sessões do banco.
- `app/models/models.py`: Define os modelos/tabelas.
- `app/routers/routes.py`: Usa o banco para armazenar conversas.

## 2. app/database/base.py

```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

- **Explicação**: Cria uma base declarativa para todos os modelos. Todos os modelos (classes) herdam de `Base` para serem mapeados para tabelas no banco.

## 3. app/database/session.py

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/agent_db"

engine = create_engine(DATABASE_URL)  # cria a conexão com o banco de dados

# cria a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

- **DATABASE_URL**: String de conexão. Formato: `mysql+pymysql://usuario:senha@host:porta/banco`.
  - `mysql+pymysql`: Driver PyMySQL para MySQL.
  - `root:root`: Usuário e senha (padrão local).
  - `localhost:3306`: Host e porta.
  - `agent_db`: Nome do banco.
- **engine**: Objeto que gerencia a conexão com o banco.
- **SessionLocal**: Fábrica de sessões. Cada sessão é uma transação isolada.

## 4. app/models/models.py

```python
from sqlalchemy import Column, Integer, Text, DateTime
from datetime import datetime, timezone
from app.database.base import Base

class Conversation(Base):
    __tablename__ = "conversations"  # define o nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)  # define a coluna 'id' como chave primária
    user_input = Column(Text, nullable=False)  # define a coluna 'user_input' para armazenar a entrada do usuário
    agent_response = Column(Text, nullable=False)  # define a coluna 'agent_response' para armazenar a resposta do agente
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))  # define a coluna 'created_at' para armazenar a data e hora de criação, com fuso horário UTC
```

- **Classe Conversation**: Representa a tabela `conversations`.
- **Campos**:
  - `id`: Chave primária, auto-incremento.
  - `user_input`: Texto da entrada do usuário (não nulo).
  - `agent_response`: Texto da resposta do agente (não nulo).
  - `created_at`: Data/hora de criação, com timezone UTC.
- **Index**: `index=True` em `id` acelera buscas.
- **Herança de Base**: Permite que SQLAlchemy crie a tabela automaticamente.

## 5. app/main.py (Parte do Banco)

```python
from app.database.base import Base
from app.database.session import engine
from app.models import models

Base.metadata.create_all(bind=engine)
```

- **create_all()**: Cria todas as tabelas definidas nos modelos (se não existirem). Executado na inicialização do app.

## 6. app/routers/routes.py (Uso do Banco)

```python
from app.database.session import SessionLocal
from app.models.models import Conversation

def get_db():
    db = SessionLocal()  # cria uma sessão do banco de dados
    try:
        yield db
    finally:
        db.close()  # fecha a sessão do banco de dados

@router.post("/agent", response_model=ConversationResponse)
def interact(data: ConversationRequest, db: Session = Depends(get_db)):
    response = agent_decision(data.user_input)

    # armazena a conversa no banco de dados
    conversation = Conversation(
        user_input=data.user_input,
        agent_response=response
    )

    db.add(conversation)  # adiciona a conversa ao banco de dados
    db.commit()  # confirma a transação no banco de dados

    return {"response": response}
```

- **get_db()**: Dependência FastAPI que fornece uma sessão de banco por requisição. Fecha automaticamente.
- **Armazenamento**: Cria um objeto `Conversation`, adiciona à sessão e commita (salva no banco).
- **Transação**: `db.commit()` persiste as mudanças.

## 7. Como Funciona o Fluxo

1. **Inicialização**: `Base.metadata.create_all()` cria tabelas.
2. **Requisição**: Endpoint `/agent` recebe dados.
3. **Processamento**: Gera resposta via LLM (Groq).
4. **Armazenamento**: Salva `user_input` e `response` na tabela `conversations`.
5. **Resposta**: Retorna JSON com a resposta.

## 8. Comandos Úteis no MySQL Workbench

- Ver tabelas: `USE agent_db; SHOW TABLES;`
- Ver dados: `SELECT * FROM conversations;`
- Estrutura da tabela: `DESCRIBE conversations;`

## 9. Alternativa para SQLite

Se quiser voltar para SQLite (sem servidor), mude `DATABASE_URL` para `"sqlite:///./agent.db"`.

## 10. Dependências

- `sqlalchemy`: ORM.
- `pymysql`: Driver MySQL.
- `cryptography`: Para autenticação MySQL.

Este código garante persistência das conversas, escalabilidade e isolamento de transações.
