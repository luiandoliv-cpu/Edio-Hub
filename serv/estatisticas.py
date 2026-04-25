from serv.tables import conexao
from datetime import date

def tempo_total(user_id):
    conn = conexao()
    cur = conn.cursor()

    cur.execute("""
        SELECT SUM(tempo_estudado)
        FROM sessoes s
        JOIN temporizadores t ON s.timer_id = t.id
        WHERE t.user_id = ?
    """, (user_id,))

    total = cur.fetchone()[0]
    conn.close()
    return total or 0

def tempo_hoje(user_id):
    hoje = date.today().isoformat()

    conn = conexao()
    cur = conn.cursor()

    cur.execute("""
        SELECT SUM(tempo_estudado)
        FROM sessoes s
        JOIN temporizadores t ON s.timer_id = t.id
        WHERE t.user_id = ? AND s.data = ?
    """, (user_id, hoje))

    total = cur.fetchone()[0]
    conn.close()
    return total or 0

def tempo_por_disciplina(user_id):
    conn = conexao()
    cur = conn.cursor()

    cur.execute("""
        SELECT d.nome, SUM(s.tempo_estudado)
        FROM sessoes s
        JOIN temporizadores t ON s.timer_id = t.id
        JOIN disciplinas d ON t.discip_id = d.discip_id
        WHERE t.user_id = ?
        GROUP BY d.nome
        ORDER BY SUM(s.tempo_estudado) DESC
    """, (user_id,))

    dados = cur.fetchall()
    conn.close()
    return dados

def disciplina_top(user_id):
    dados = tempo_por_disciplina(user_id)
    if not dados:
        return None
    return dados[0][0]

def streak_estudo(user_id):
    conn = conexao()
    cur = conn.cursor()

    cur.execute("""
        SELECT DISTINCT substr(s.data, 1, 10)
        FROM sessoes s
        JOIN temporizadores t ON s.timer_id = t.id
        WHERE t.user_id = ?
        ORDER BY substr(s.data, 1, 10) DESC
    """, (user_id,))

    datas = [d[0] for d in cur.fetchall()]
    conn.close()

    from datetime import date, timedelta

    streak = 0
    dia = date.today()

    for d in datas:
        if d == dia.isoformat():
            streak += 1
            dia -= timedelta(days=1)
        else:
            break

    return streak