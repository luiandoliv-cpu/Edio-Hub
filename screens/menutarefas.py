from serv.todo import *
from serv.utils import limpar_tela
import time

def menu_todo(user_id):
    while True:
        print("\n===== To-Do =====")
        print("1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Excluir tarefa")
        print("0 - Voltar ao menu principal")

        op = input("Escolha: ")

        if op == "1":
            desc = input("Descrição da tarefa: ")
            sucesso, msg = criar_tarefa(user_id, desc)
            print(msg)

        elif op == "2":
            tarefas = listar_tarefas(user_id)
            mostrar_tarefas(tarefas)

        elif op == "3":
            tarefas = listar_tarefas(user_id)
            if not mostrar_tarefas(tarefas):
                continue

            tid = input("ID da tarefa concluída: ")
            if not tid.isdigit():
                print("ID inválido.")
                continue

            print(concluir_tarefa(user_id, int(tid))[1])

        elif op == "4":
            tarefas = listar_tarefas(user_id)
            if not mostrar_tarefas(tarefas):
                continue

            tid = input("ID da tarefa para excluir: ")
            if not tid.isdigit():
                print("ID inválido.")
                continue

            print(excluir_tarefa(user_id, int(tid))[1])

        elif op == "0":
            limpar_tela()
            break

        else:
            print("Opção inválida.")
            time.sleep(2)
            limpar_tela()

