from serv.tables import conexao
from serv.auth import verificar_senha, hash_senha
from serv.sessao import limpar_sessao
import re

def validar_username(username):
    username = username.strip()
    if len(username) < 5:
        return False, "Username deve ter no mínimo 5 caracteres."
    return True, ""

def validar_senha(senha):
    if len(senha) < 4 or len(senha) > 12:
        return False, "Senha deve ter entre 4 e 12 caracteres."

    if not re.search(r"[A-Z]", senha):
        return False, "Senha precisa de letra maiúscula."

    if not re.search(r"\d", senha):
        return False, "Senha precisa de número."

    if not re.search(r"[!@#$%^&*()_+=\-{};:'\",.<>?/]", senha):
        return False, "Senha precisa de caractere especial."

    return True, ""

def editar_username(user_id, novo_username, senha_atual):
    conn = conexao()
    cur = conn.cursor()

    # buscar senha atual
    cur.execute("SELECT password FROM users WHERE user_id=?", (user_id,))
    senha_hash = cur.fetchone()[0]

    if not verificar_senha(senha_atual, senha_hash):
        conn.close()
        return False, "Senha incorreta."

    valido, msg = validar_username(novo_username)
    if not valido:
        conn.close()
        return False, msg

    try:
        cur.execute(
            "UPDATE users SET username=? WHERE user_id=?",
            (novo_username, user_id)
        )
        conn.commit()
        return True, "Username atualizado!"
    except:
        return False, "Username já existe."
    finally:
        conn.close()

def editar_senha(user_id, senha_atual, nova_senha):
    conn = conexao()
    cur = conn.cursor()

    cur.execute("SELECT password FROM users WHERE user_id=?", (user_id,))
    senha_hash = cur.fetchone()[0]

    if not verificar_senha(senha_atual, senha_hash):
        conn.close()
        return False, "Senha atual incorreta."

    valido, msg = validar_senha(nova_senha)
    if not valido:
        conn.close()
        return False, msg

    nova_hash = hash_senha(nova_senha)

    cur.execute(
        "UPDATE users SET password=? WHERE id=?",
        (nova_hash, user_id)
    )

    conn.commit()
    conn.close()
    return True, "Senha atualizada com sucesso!"

def excluir_conta(user_id, senha_atual):
    conn = conexao()
    cur = conn.cursor()

    cur.execute("SELECT password FROM users WHERE user_id=?", (user_id,))
    resultado = cur.fetchone()

    if not resultado:
        conn.close()
        return False, "Usuário não encontrado", False

    if not verificar_senha(senha_atual, resultado[0]):
        conn.close()
        return False, "Senha incorreta", False

    cur.execute("DELETE FROM users WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

    limpar_sessao()  # 👈 importante
    return True, "Conta excluída com sucesso", True