import bcrypt
import re
import sqlite3
from serv.tables import conexao
from serv.sessao import salvar_sessao

def hash_senha(senha: str) -> bytes:
    '''Define a hashificação de senha'''
    senha_bytes = senha.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha_bytes, salt)
    return hashed

def verificar_senha(senha_digitada: str, senha_hash: bytes) -> bool:
    '''Verifica se a senha digitada no coincide com o hash de senha no login'''
    return bcrypt.checkpw(senha_digitada.encode("utf-8"), senha_hash)

def validar_cadastro(username, password):
    '''Define as validações de username e senha na criação de cadastro'''
    if len(username) < 5:
        return False, "Usuário precisa ter pelo menos 5 caracteres"

    if len(password) < 4 or len(password) > 18:
        return False, "Senha precisa ter pelo menos 6 caracteres e, no máximo, 18 caracteres"
    
    if not re.search(r"[A-Z]", password):
        return False, "Senha precisa ter pelo menos 1 letra maiúscula"

    if not re.search(r"[0-9]", password):
        return False, "Senha precisa ter pelo menos 1 número"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\]]", password):
        return False, "Senha precisa ter pelo menos 1 caractere especial"
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return False, "Usuário já existe"

    conn.close()
    return True, "OK"

def registrar_usuario(username, password):
    '''Etapa de validar a criação de conta do usuário'''
    valido, msg = validar_cadastro(username, password)
    if not valido:
        return False, msg, None

    senha_hash = hash_senha(password)

    conn = conexao()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, senha_hash)
        )
        conn.commit()

        user_id = cursor.lastrowid
        salvar_sessao(user_id)
        return True, "Conta criada com sucesso!", user_id

    except sqlite3.Error as e:
        return False, f"Erro: {e}", None
    finally:
        conn.close()

def login_usuario(username, password):
    '''Etapa de validação de login em conta já existente pelo usuário'''
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_id, password FROM users WHERE username = ?",
        (username,)
    )
    resultado = cursor.fetchone()
    conn.close()

    if not resultado:
        return False, "Usuário não encontrado", None

    user_id, senha_hash = resultado

    if verificar_senha(password, senha_hash):
        salvar_sessao(user_id)
        return True, "Login realizado com sucesso!", user_id
        
    else:
        return False, "Senha incorreta", None