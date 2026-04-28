import sqlite3

def conexao():
    '''Faz conexão com o banco'''
    return sqlite3.connect("accko.db")

def criar_tabelas():
    '''Cria tabelas do banco'''
    conn = conexao()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password BLOB NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS disciplinas(
        discip_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        nome TEXT NOT NULL
    )""")

    cursor.execute("""
 CREATE TABLE IF NOT EXISTS temporizadores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    discip_id INTEGER NOT NULL,
    tempo_estudo INTEGER NOT NULL,
    tempo_pausa INTEGER DEFAULT 0
)
""")

    cursor.execute("""
  CREATE TABLE IF NOT EXISTS sessoes(
    user_id INTEGER,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timer_id INTEGER,
    tempo_estudado INTEGER,
    data TEXT NOT NULL
    )
   """)


    cursor.execute("""
  CREATE TABLE IF NOT EXISTS tarefas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        descricao TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Pendente'
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS anexos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        mensagem TEXT NOT NULL
    )""")

    conn.commit()
    conn.close()
criar_tabelas()
