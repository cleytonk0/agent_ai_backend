from groq import Groq
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente Groq com a chave de API obtida das variáveis de ambiente
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    client = Groq(api_key=api_key)
    print(f"Groq API Key loaded: {api_key[:10]}...")
else:
    print("ERROR: GROQ_API_KEY not found in environment variables!")
    client = None

def generate_response(prompt: str) -> str:
    """Gera uma resposta usando o modelo Llama 3.1 via Groq com base no prompt fornecido."""
    if not client:
        return "Erro: Cliente Groq não inicializado. Verifique a chave da API."
    try:
        print(f"Generating response for prompt: {prompt}")  # Debug
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Você é um assistente técnico."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Error in generate_response: {e}")  # Debug
        return f"Erro ao gerar resposta: {str(e)}"