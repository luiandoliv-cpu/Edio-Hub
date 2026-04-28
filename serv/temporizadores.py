import sqlite3
import time
from datetime import datetime, date
from serv.tables import conexao
from serv.utils import limpar_tela

def criar_temporizador(user_id, nome, discip_id, estudo, pausa):
    '''Cria temporizador no banco'''
    nome = nome.strip()

    if len(nome) < 1:
        return False, "Nome precisa ter ao menos 1 caractere."

    try:
        estudo = int(estudo)
    except:
        return False, "Tempo de estudo inválido."

    try:
        pausa = int(pausa)
    except:
        pausa = 0

    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO temporizadores (user_id, nome, discip_id, tempo_estudo, tempo_pausa)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, nome, discip_id, int(estudo), pausa))

    conn.commit()
    conn.close()
    return True, "Temporizador criado!"

def listar_temporizadores(user_id):
    '''Lista temporizadores existentes'''
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
    '''Contagem da sessão de estudos'''
    total_segundos = minutos * 60

    print("\nPressione CTRL+C para encerrar.\n")

    try:
        while total_segundos:
            mins = total_segundos // 60
            segs = total_segundos % 60
            print(f"\r{mins:02d}:{segs:02d}", end="")
            time.sleep(1)
            total_segundos -= 1

        time.sleep(1)
        limpar_tela()
        print("\nTempo finalizado!")
        time.sleep(1)
        limpar_tela()
        return True

    except KeyboardInterrupt:
        time.sleep(1)
        limpar_tela()
        print("\n Encerrado pelo usuário!")
        return False
    
def iniciar_temporizador(user_id, timer_id):
    '''Iniciar temporizador'''
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT tempo_estudo, tempo_pausa FROM temporizadores
        WHERE id = ? AND user_id = ?
    """, (timer_id, user_id))

    timer = cursor.fetchone()

    if timer is None:
     conn.close()
     return False, "Temporizador não encontrado."

    if not timer:
        conn.close()
        print("Temporizador não encontrado.")
        time.sleep(1)
        limpar_tela()

    estudo, pausa = timer
    total_estudado = 0

    print("\n Temporizador iniciado!")
    print("CTRL+C para encerrar a qualquer momento.")

    try:
        while True:
            # estudo
            print("\n Estudando...")
            terminou = contagem_interrompivel(estudo)

            if not terminou:
                break

            total_estudado += estudo

            # pausa
            if pausa > 0:
                print("\n Hora de fazer uma pausa...")
                terminou = contagem_interrompivel(pausa)
                if not terminou:
                    break

    except KeyboardInterrupt:
        pass

    # salvar total estudado
    if total_estudado > 0:
     salvar_sessao(user_id, timer_id, total_estudado)

    conn.close()

    return True, f"Sessão encerrada! Você estudou {total_estudado} minutos 🎉"

def editar_temporizador(user_id, timer_id, estudo, pausa):
    '''Alterar características do temporizador'''
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
    '''Apaga temporizador da conta'''
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

def listar_disciplinas(user_id):
    '''Lista disciplinas para escolha de disciplina ao temporizador'''
    conn = conexao()
    cur = conn.cursor()
    cur.execute("SELECT discip_id, nome FROM disciplinas WHERE user_id=?", (user_id,))
    dados = cur.fetchall()
    conn.close()
    return dados

def salvar_sessao(user_id, timer_id, tempo_estudado):
    '''Salva sessões de estudos e suas durações'''
    conn = conexao()
    cursor = conn.cursor()

    data_hoje = date.today().isoformat()

    cursor.execute("""
        INSERT INTO sessoes (timer_id, user_id, tempo_estudado, data)
        VALUES (?, ?, ?, ?)
    """, (timer_id, user_id, tempo_estudado, data_hoje))

    conn.commit()
    conn.close()