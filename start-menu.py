from auth import registrar_usuario, login_usuario
from menuprincip import menu_principal
import time
from utils import limpar_tela

def tela_inicial():
    while True:
        print("\n===== BEM VINDO =====")
        print("1 - Criar conta")
        print("2 - Fazer login")
        print("3 - Sair")

        op = input("Escolha: ")

        # CADASTRO
        if op == "1":
            limpar_tela()
            username = input("Username: ")
            senha = input("Senha: ")

            sucesso, msg, user_id = registrar_usuario(username, senha)
            print(msg)

            if sucesso:
                print("Entrando...")
                time.sleep(3)
                limpar_tela()
                menu_principal(user_id)

        # LOGIN
        elif op == "2":
            limpar_tela()
            username = input("Username: ")
            senha = input("Senha: ")

            sucesso, msg, user_id = login_usuario(username, senha)
            print(msg)

            if sucesso:
                print("Entrando...")
                time.sleep(3)
                limpar_tela()
                menu_principal(user_id)

        elif op == "3":
            print("Até logo!")
            time.sleep(1)
            limpar_tela()
            break
        else:
            print("Opção inválida")
            time.sleep(1)
            limpar_tela()
tela_inicial()
