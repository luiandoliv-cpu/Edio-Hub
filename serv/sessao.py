import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO_SESSAO = os.path.join(BASE_DIR, "sessao.json")

def salvar_sessao(user_id):
    with open(ARQUIVO_SESSAO, "w") as f:
        json.dump({"user_id": user_id}, f)

def carregar_sessao():
    if not os.path.exists(ARQUIVO_SESSAO):
        return None
    
    with open(ARQUIVO_SESSAO, "r") as f:
        dados = json.load(f)
        return dados.get("user_id")

def limpar_sessao():
    if os.path.exists(ARQUIVO_SESSAO):
        os.remove(ARQUIVO_SESSAO)