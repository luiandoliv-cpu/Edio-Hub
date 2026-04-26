from serv.auth import registrar_usuario, login_usuario
from screens.menuprincip import menu_principal
import time
from serv.utils import limpar_tela

def tela_inicial():
    while True:
        print("\n===== Bem-vindo ao EdioHub =====")
        print("1 - Criar conta")
        print("2 - Entrar")
        print("3 - Sair")

        op = input("Escolha: ")

        if op == "1":
            limpar_tela()
            username = input("Username: ")
            senha = input("Senha: ")

            sucesso, msg, user_id = registrar_usuario(username, senha)
            print(msg)

            if sucesso:
                print("Entrando...")
                time.sleep(2)
                limpar_tela()
                return user_id   

        elif op == "2":
            limpar_tela()
            username = input("Username: ")
            senha = input("Senha: ")

            sucesso, msg, user_id = login_usuario(username, senha)
            print(msg)

            if sucesso:
                print("Entrando...")
                time.sleep(2)
                limpar_tela()
                return user_id  

        elif op == "3":
            print("Até logo!")
            time.sleep(1)
            limpar_tela()
            return "exit"       

        else:
            print("Opção inválida")
            time.sleep(1)
            limpar_tela()