import sqlite3
from serv.tables import conexao

def listar_disciplinas(user_id):
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, nome FROM disciplinas WHERE user_id = ?",
        (user_id,)
    )

    disciplinas = cursor.fetchall()
    conn.close()
    return disciplinas

def criar_disciplina(user_id, nome):
    nome = nome.strip()

    if nome == "":
        return False, "Nome não pode ser vazio."

    conn = conexao()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO disciplinas (nome, user_id) VALUES (?, ?)",
        (nome, user_id)
    )

    conn.commit()
    conn.close()

    return True, "Disciplina criada com sucesso!"

def editar_disciplina(user_id, disciplina_id, novo_nome):
    if not novo_nome or novo_nome.strip() == "":
        return False, "Nome não pode ser vazio"

    conn = conexao()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE disciplinas SET nome = ? WHERE id = ? AND user_id = ?",
        (novo_nome, disciplina_id, user_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return False, "Disciplina não encontrada"

    conn.close()
    return True, "Disciplina atualizada!"

def excluir_disciplina(user_id, disciplina_id):
    conn = conexao()
    cursor = conn.cursor()

    # remove disciplina
    cursor.execute(
        "DELETE FROM disciplinas WHERE id = ? AND user_id = ?",
        (disciplina_id, user_id)
    )

    if cursor.rowcount == 0:
        conn.close()
        return False, "Disciplina não encontrada."

    conn.commit()
    conn.close()
    return True, "Disciplina excluída com sucesso!"