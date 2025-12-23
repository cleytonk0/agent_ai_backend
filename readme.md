# AI Agent Backend

Um backend robusto e escalável para um agente de IA conversacional, desenvolvido com FastAPI e integrado com modelos de linguagem avançados (Groq/Llama). Permite interações inteligentes, armazenamento de histórico de conversas ao banco de dados (MySQL) e fácil expansão.

## 🚀 Funcionalidades

- **Interação com IA**: Respostas geradas por modelos de linguagem (Groq com Llama 3.1).
- **Armazenamento de Conversas**: Histórico persistido em banco de dados (MySQL).
- **API RESTful**: Endpoints documentados com Swagger UI.
- **Segurança**: Credenciais protegidas via variáveis de ambiente.
- **Escalabilidade**: Arquitetura modular para fácil manutenção e expansão.

## 🛠️ Tecnologias Utilizadas

- **Backend**: FastAPI (Python)
- **Banco de Dados**: SQLAlchemy + MySQL
- **IA**: Groq API (Llama 3.1-8b-instant)
- **Autenticação**: Variáveis de ambiente (.env)
- **Documentação**: Swagger UI (automática)
- **Gerenciamento de Dependências**: pip + requirements.txt


## 🗂️ Estrutura do Projeto

```
ai-agent-backend/
├── app/
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── database/
│   │   ├── base.py          # Base SQLAlchemy
│   │   └── session.py       # Configuração de conexão DB
│   ├── models/
│   │   └── models.py        # Modelos de dados
│   ├── routers/
│   │   └── routes.py        # Endpoints da API
│   ├── services/
│   │   └── llm_service.py   # Integração com IA
│   └── schemas/
│       └── conversation.py  # Schemas Pydantic
├── .env.example             # Template de variáveis de ambiente
├── .gitignore                
├── requirements.txt         # Dependências Python
├── DATABASE_EXPLANATION.md  # Documentação do banco de dados
└── README.md                

Estou em desenvolvimento...
