import sqlite3
from tables import conexao

def criar_tarefa(user_id, descricao):
    descricao = descricao.strip()

    if len(descricao) < 1:
        return False, "A tarefa precisa ter pelo menos 1 caractere."

    conn = conexao()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tarefas (user_id, descricao) VALUES (?, ?)",
        (user_id, descricao)
    )

    conn.commit()
    conn.close()

    return True, "Tarefa criada com sucesso!"

def listar_tarefas(user_id):
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, descricao, status FROM tarefas WHERE user_id = ?",
        (user_id,)
    )

    tarefas = cursor.fetchall()
    conn.close()

    return tarefas

def concluir_tarefa(user_id, tarefa_id):
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id = ? AND user_id = ?",
        (tarefa_id, user_id)
    )

    if cursor.rowcount == 0:
        conn.close()
        return False, "Tarefa não encontrada."

    conn.commit()
    conn.close()
    return True, "Tarefa concluída 🎉"

def excluir_tarefa(user_id, tarefa_id):
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id = ? AND user_id = ?",
        (tarefa_id, user_id)
    )

    if cursor.rowcount == 0:
        conn.close()
        return False, "Tarefa não encontrada."

    conn.commit()
    conn.close()
    return True, "Tarefa excluída."

def mostrar_tarefas(tarefas):
    if not tarefas:
        print("\nVocê não possui tarefas.")
        return False

    print("\n===== SUAS TAREFAS =====")
    print("ID | Descrição | Status")
    print("-------------------------")

    for t in tarefas:
        print(f"{t[0]} | {t[1]} | {t[2]}")

    return True