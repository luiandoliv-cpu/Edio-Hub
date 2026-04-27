from serv.utils import limpar_tela
from screens.menudiscip import menu_disciplinas
from screens.menutarefas import menu_todo
from screens.menutempo import menu_temporizadores
from screens.menuanex import menu_mural
from screens.menuestat import menu_estatisticas, formatar
from screens.menuconta import tela_conta
from serv.sessao import limpar_sessao
from serv.estatisticas import resumo_boas_vindas
import time

def menu_principal(user_id):
    while True:
        hoje, streak, top = resumo_boas_vindas(user_id)

        print("\n Bem-vindo!")
        print(f"Hoje você estudou: {formatar(hoje)}")
        print(f"Streak: {streak} dias 🔥")
        print(f"Foco atual: {top or 'Escolha uma disciplina'}")
        print("1 - Disciplinas")
        print("2 - Temporizadores")
        print("3 - To-Do")
        print("4 - Estatatísticas")
        print("5 - Gerenciar conta")
        print("0 - Logout")
    
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
            print("Opção inválida")
            time.sleep(2)
            limpar_tela()
