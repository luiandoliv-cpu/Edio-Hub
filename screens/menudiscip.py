from serv.disciplinas import *
from serv.utils import limpar_tela
import time

def menu_disciplinas(user_id):
    while True:
        limpar_tela()
        print("\n===== Disciplinas =====")
        print("1 - Criar disciplina")
        print("2 - Listar disciplinas")
        print("3 - Editar disciplina")
        print("4 - Excluir disciplina")
        print("0 - Voltar ao menu principal")

        op = input("Escolha: ")

        if op == "1":
         limpar_tela()
         nome = input("Nome da disciplina: ")
         sucesso, msg = criar_disciplina(user_id, nome)
         print(msg)
         time.sleep(2)
         limpar_tela()

        elif op == "2":
            limpar_tela()
            disciplinas = listar_disciplinas(user_id)

            if not disciplinas:
                print("Nenhuma disciplina cadastrada")
            else:
                for d in disciplinas:
                    print(f"{d[0]} - {d[1]}")
                    time.sleep(12)
                    limpar_tela()


        elif op == "3":
            limpar_tela()
            disciplinas = listar_disciplinas(user_id)

            if not disciplinas:
                print("Nenhuma disciplina para editar")
                continue

            for d in disciplinas:
                print(f"{d[0]} - {d[1]}")
            
            time.sleep(6)
            limpar_tela()
            did = input("ID da disciplina: ")
            novo_nome = input("Novo nome: ")
            print(editar_disciplina(user_id, did, novo_nome)[1])
            time.sleep(3)
            limpar_tela()

        elif op == "4":
            limpar_tela()
            disciplinas = listar_disciplinas(user_id)

            if not disciplinas:
                print("Nenhuma disciplina para excluir")
                continue

            for d in disciplinas:
                print(f"{d[0]} - {d[1]}")

            time.sleep(6)
            limpar_tela()
            did = input("ID da disciplina: ")
            sucesso, msg = excluir_disciplina(user_id, did)
            print(msg)
            time.sleep(3)
            limpar_tela()

        elif op == "0":
            limpar_tela()
            break

        else:
            print("Opção inválida")
            time.sleep(2)
            limpar_tela()
