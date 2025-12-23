from app.services.llm_service import generate_response

def agent_decision(user_input: str) -> str:
    """
    Decide como responder ao usuaário
    """
    if "status" in user_input.lower():
        return "Ferramenta: consulta de status ainda não implementada"
    
    return generate_response(user_input)