from serv.auth import registrar_usuario, login_usuario
from screens.menuprincip import menu_principal
import time
from serv.utils import *

def tela_inicial():

    while True:
        limpar_tela()
        print(azul("\n===== Bem-vindo ao EdioHub ====="))
        print(verde("1 - Criar conta"))
        print(amarelo("2 - Entrar"))
        print(vermelho("3 - Sair"))

        op = input("Escolha: ")

        if op == "1":
            limpar_tela()
            username = input("Username: ")
            senha = input("Senha: ")

            sucesso, msg, user_id = registrar_usuario(username, senha)
            print(msg)

            if sucesso:
              pausa_auto(verde("Conta criada com sucesso!"), 2)
              return user_id
            else:
              time.sleep(2)
              limpar_tela()
              continue

        elif op == "2":
            limpar_tela()
            username = input("Username: ")
            senha = input("Senha: ")

            sucesso, msg, user_id = login_usuario(username, senha)
            print(msg)

            if sucesso:
              pausa_auto(verde("Login realizado com sucesso!"), 2)
              return user_id
            else:
               time.sleep(2)
               limpar_tela()
               continue

        elif op == "3":
            print(ciano("Até logo! :)"))
            time.sleep(1)
            limpar_tela()
            return "exit"       

        else:
            print(amarelo("Opção inválida"))
            time.sleep(1)
            limpar_tela()