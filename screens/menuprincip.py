from serv.utils import *
from screens.menudiscip import menu_disciplinas
from screens.menutarefas import menu_todo
from screens.menutempo import menu_temporizadores
from screens.menuestat import menu_estatisticas, formatar
from screens.menuconta import tela_conta
from serv.sessao import limpar_sessao
from serv.estatisticas import resumo_boas_vindas
import time

def menu_principal(user_id):
    '''Define a tela do menu principal do usuário'''
    while True:
        hoje, streak, top = resumo_boas_vindas(user_id)

        print(azul("\n Bem-vindo!"))
        print(verde(f"Hoje você estudou: {formatar(hoje)}"))
        print(amarelo(f"Streak: {streak} dias 🔥"))
        print(f"Foco atual: {top or 'Escolha uma disciplina'}")
        print("1 - Disciplinas")
        print("2 - Temporizadores")
        print("3 - To-Do")
        print("4 - Estatatísticas")
        print("5 - Gerenciar conta")
        print(vermelho("0 - Logout"))
    
        op = input("Escolha: ")

        if op == "1":
            menu_disciplinas(user_id)

        elif op == "2":
            menu_temporizadores(user_id)

        elif op == "3":
            menu_todo(user_id)

        elif op == "4":
            menu_estatisticas(user_id)

        elif op == "5":
            resultado = tela_conta(user_id)

            if resultado == "logout":
                return
            
        elif op == "0":
            limpar_sessao()
            limpar_tela()
            print("Logout realizado.")
            time.sleep(2)
            limpar_tela()
            return None

        else:
            print(amarelo("Opção inválida"))
            time.sleep(2)
            limpar_tela()
