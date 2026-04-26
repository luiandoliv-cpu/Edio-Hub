from serv.utils import limpar_tela
from screens.menudiscip import menu_disciplinas
from screens.menutarefas import menu_todo
from screens.menutempo import menu_temporizadores
from screens.menuanex import menu_mural
from screens.menuestat import menu_estatisticas
from serv.sessao import limpar_sessao
import time

def menu_principal(user_id):
    while True:
        print("\n===== Menu Principal =====")
        print("1 - Disciplinas")
        print("2 - Temporizadores")
        print("3 - To-Do")
        print("4 - Estatatísticas")
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

        elif op == "0":
            limpar_sessao()
            print("Logout realizado.")
            time.sleep(2)
            limpar_tela()
            return None

        else:
            print("Opção inválida")
            time.sleep(2)
            limpar_tela()
