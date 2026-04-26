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
        SELECT DISTINCT substr(s.data,1,10)
        FROM sessoes s
        JOIN temporizadores t ON s.timer_id = t.id
        WHERE t.user_id = ?
        ORDER BY s.data DESC
    """, (user_id,))

    datas = [d[0] for d in cur.fetchall()]
    conn.close()

    if not datas:
        return 0

    from datetime import date, timedelta

    hoje = date.today()
    ontem = hoje - timedelta(days=1)

    datas_set = set(datas)

    # streak pode começar hoje OU ontem
    if hoje.isoformat() in datas_set:
        dia = hoje
    elif ontem.isoformat() in datas_set:
        dia = ontem
    else:
        return 0

    streak = 0

    while dia.isoformat() in datas_set:
        streak += 1
        dia -= timedelta(days=1)

    return streak

def resumo_boas_vindas(user_id):
    hoje = tempo_hoje(user_id)
    streak = streak_estudo(user_id)
    top = disciplina_top(user_id)

    return hoje, streak, top

def top_3_disciplinas(user_id):
    conn = conexao()
    cur = conn.cursor()

    cur.execute("""
        SELECT d.nome, SUM(s.tempo_estudado) as total
        FROM sessoes s
        JOIN temporizadores t ON s.timer_id = t.id
        JOIN disciplinas d ON t.discip_id = d.discip_id
        WHERE t.user_id = ?
        GROUP BY d.nome
        ORDER BY total DESC
        LIMIT 3
    """, (user_id,))

    dados = cur.fetchall()
    conn.close()
    return dados