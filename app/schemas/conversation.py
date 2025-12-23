#Cria schemas para requisições e respostas de conversação
from pydantic import BaseModel #impota a classe BaseModel do pydantic

class ConversationRequest(BaseModel):
    user_input: str # define o campo 'user_input' como uma string


class ConversationResponse(BaseModel):
    response: str # define o campo 'response' como uma string