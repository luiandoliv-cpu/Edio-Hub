from serv.conta import *
from serv.utils import limpar_tela
from serv.sessao import limpar_sessao
import time

def tela_conta(user_id):
    while True:
        limpar_tela()
        print("\n===== MINHA CONTA =====")
        print("1 - Alterar username")
        print("2 - Alterar senha")
        print("3 - Excluir conta")
        print("0 - Voltar")

        op = input("Escolha: ")

        # EDITAR USERNAME
        if op == "1":
            limpar_tela()
            novo = input("Novo username: ")
            senha = input("Confirme sua senha: ")
            sucesso, msg = editar_username(user_id, novo, senha)
            print(msg)
            input("\nENTER...")

        # EDITAR SENHA
        elif op == "2":
            limpar_tela()
            atual = input("Senha atual: ")
            nova = input("Nova senha: ")
            sucesso, msg = editar_senha(user_id, atual, nova)
            print(msg)
            input("\nENTER...")

        # EXCLUIR CONTA
        elif op == "3":
          limpar_tela()
          print("ATENÇÃO! A conta não poderá ser recuperada após deletada")
          senha = input("Confirme sua senha: ")

          sucesso, msg, logout = excluir_conta(user_id, senha)
          print(msg)
          input("Pressione ENTER...")
          limpar_tela()

          if logout:
           return "logout"
          
        elif op == "0":
           limpar_tela()
           break