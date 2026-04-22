import sqlite3
from serv.tables import conexao

def criar_anexo(user_id):
    titulo = input("Título do lembrete: ").strip()
    if len(titulo) == 0:
        return False, "Título deve ter pelo menos 1 caractere."

    mensagem = input("Mensagem: ").strip()
    if len(mensagem) == 0:
        return False, "Mensagem deve ter pelo menos 1 caractere."

    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO anexos (user_id, titulo, mensagem)
        VALUES (?, ?, ?)
    """, (user_id, titulo, mensagem))

    conn.commit()
    conn.close()

    return True, "Lembrete criado com sucesso!"

def listar_anexos(user_id):
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titulo, mensagem
        FROM anexos
        WHERE user_id = ?
    """, (user_id,))

    anexos = cursor.fetchall()
    conn.close()
    return anexos

def excluir_anexo(user_id):
    anexos = listar_anexos(user_id)

    if not anexos:
        print("Nenhum lembrete para excluir.")
        return

    print("\n--- MURAL ---")
    for a in anexos:
        print(f"{a[0]} - {a[1]}")

    try:
        aid = int(input("ID do lembrete: "))
    except ValueError:
        print("ID inválido.")
        return

    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM anexos
        WHERE id = ? AND user_id = ?
    """, (aid, user_id))

    if cursor.rowcount == 0:
        print("Lembrete não encontrado.")
    else:
        print("Lembrete excluído!")

    conn.commit()
    conn.close()