from todo import criar_tarefa, concluir_tarefa, excluir_tarefa, listar_tarefas, mostrar_tarefas

def menu_todo(user_id):
    while True:
        print("\n===== TO-DO LIST =====")
        print("1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Excluir tarefa")
        print("5 - Voltar ao menu principal")

        op = input("Escolha: ")

        # CRIAR
        if op == "1":
            desc = input("Descrição da tarefa: ")
            sucesso, msg = criar_tarefa(user_id, desc)
            print(msg)

        # LISTAR
        elif op == "2":
            tarefas = listar_tarefas(user_id)
            mostrar_tarefas(tarefas)

        # CONCLUIR
        elif op == "3":
            tarefas = listar_tarefas(user_id)
            if not mostrar_tarefas(tarefas):
                continue

            tid = input("ID da tarefa concluída: ")
            if not tid.isdigit():
                print("ID inválido.")
                continue

            print(concluir_tarefa(user_id, int(tid))[1])

        # EXCLUIR
        elif op == "4":
            tarefas = listar_tarefas(user_id)
            if not mostrar_tarefas(tarefas):
                continue

            tid = input("ID da tarefa para excluir: ")
            if not tid.isdigit():
                print("ID inválido.")
                continue

            print(excluir_tarefa(user_id, int(tid))[1])

        elif op == "5":
            break

        else:
            print("Opção inválida.")
