from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.conversation import ConversationRequest, ConversationResponse
from app.agent.agent import agent_decision
from app.database.session import SessionLocal 
from app.models.models import Conversation

#cria uma instância 
router = APIRouter()

def get_db():
    db = SessionLocal() # cria uma sessão do banco de dados
    try:
        yield db
    finally:
        db.close() # fecha a sessão do banco de dados
    
# define a rota POST /agent para interagir com o agente
@router.post("/agent", response_model=ConversationResponse)

# função para interagir com o agente
def interact(
    data: ConversationRequest,
    db: Session = Depends(get_db)
):
    response = agent_decision(data.user_input) # obtém a resposta do agente

    # armazena a conversa no banco de dados
    conversation = Conversation(
        user_input=data.user_input,
        agent_response=response
    )

    db.add(conversation) # adiciona a conversa ao banco de dados
    db.commit() # confirma a transação no banco de dados

    return {"response": response} # retorna a resposta do agente