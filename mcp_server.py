from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI(title="MCP Test Server")

# Permite acesso de qualquer origem (útil para testes locais)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exemplo de lista de recursos
resources = [
    {"id": "1", "name": "Recurso de Exemplo", "description": "Este é um recurso de teste."},
    {"id": "2", "name": "Outro Recurso", "description": "Outro recurso para testar o MCP."}
]

@app.get("/resources")
def list_resources():
    """Lista todos os recursos disponíveis."""
    return resources

@app.get("/resources/{resource_id}")
def get_resource(resource_id: str):
    """Retorna um recurso específico pelo ID."""
    for r in resources:
        if r["id"] == resource_id:
            return r
    return {"error": "Resource not found"}, 404

@app.get("/")
def root():
    return {"status": "MCP Test Server rodando!"}

