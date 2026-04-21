import sqlite3
import time
from datetime import datetime
from tables import conexao

def criar_temporizador(user_id, nome, estudo, pausa):
    nome = nome.strip()

    if len(nome) < 1:
        return False, "Nome precisa ter ao menos 1 caractere."

    if not estudo.isdigit() or int(estudo) <= 0:
        return False, "Tempo de estudo inválido."

    pausa = int(pausa) if pausa.isdigit() else 0

    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO temporizadores (user_id, nome, tempo_estudo, tempo_pausa)
        VALUES (?, ?, ?, ?)
    """, (user_id, nome, int(estudo), pausa))

    conn.commit()
    conn.close()
    return True, "Temporizador criado!"

def listar_temporizadores(user_id):
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, tempo_estudo, tempo_pausa
        FROM temporizadores
        WHERE user_id = ?
    """, (user_id,))

    timers = cursor.fetchall()
    conn.close()
    return timers

def contagem_interrompivel(minutos):
    total_segundos = minutos * 60

    print("\nPressione CTRL+C para encerrar.\n")

    try:
        while total_segundos:
            mins = total_segundos // 60
            segs = total_segundos % 60
            print(f"\r⏱️ {mins:02d}:{segs:02d}", end="")
            time.sleep(1)
            total_segundos -= 1

        print("\nTempo finalizado!")
        return True

    except KeyboardInterrupt:
        print("\n⛔ Encerrado pelo usuário!")
        return False
    
def iniciar_temporizador(user_id, timer_id):
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT tempo_estudo, tempo_pausa FROM temporizadores
        WHERE id = ? AND user_id = ?
    """, (timer_id, user_id))

    timer = cursor.fetchone()

    if not timer:
        conn.close()
        return False, "Temporizador não encontrado."

    estudo, pausa = timer
    total_estudado = 0

    print("\n🚀 Temporizador iniciado!")
    print("CTRL+C para encerrar a qualquer momento.")

    try:
        while True:
            # estudo
            print("\n📚 Estudando...")
            terminou = contagem_interrompivel(estudo)

            if not terminou:
                break

            total_estudado += estudo

            # pausa
            if pausa > 0:
                print("\n☕ Pausa...")
                terminou = contagem_interrompivel(pausa)
                if not terminou:
                    break

    except KeyboardInterrupt:
        pass

    # salvar total estudado
    if total_estudado > 0:
        cursor.execute("""
            INSERT INTO sessoes (timer_id, tempo_estudado, data)
            VALUES (?, ?, ?)
        """, (timer_id, total_estudado,
              datetime.now().strftime("%d/%m/%Y %H:%M")))

        conn.commit()

    conn.close()

    return True, f"Sessão encerrada! Você estudou {total_estudado} minutos 🎉"

def editar_temporizador(user_id, timer_id, estudo, pausa):
    if not estudo.isdigit() or int(estudo) <= 0:
        return False, "Tempo de estudo inválido."

    pausa = int(pausa) if pausa.isdigit() else 0

    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE temporizadores
        SET tempo_estudo = ?, tempo_pausa = ?
        WHERE id = ? AND user_id = ?
    """, (int(estudo), pausa, timer_id, user_id))

    if cursor.rowcount == 0:
        conn.close()
        return False, "Temporizador não encontrado."

    conn.commit()
    conn.close()
    return True, "Temporizador atualizado!"

def excluir_temporizador(user_id, timer_id):
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM temporizadores WHERE id=? AND user_id=?",
        (timer_id, user_id)
    )

    if cursor.rowcount == 0:
        conn.close()
        return False, "Temporizador não encontrado."

    conn.commit()
    conn.close()
    return True, "Temporizador excluído!"
