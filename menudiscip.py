from disciplinas import criar_disciplina, listar_disciplinas, excluir_disciplina, editar_disciplina

def menu_disciplinas(user_id):
    while True:
        print("\n===== DISCIPLINAS =====")
        print("1 - Criar disciplina")
        print("2 - Listar disciplinas")
        print("3 - Editar disciplina")
        print("4 - Excluir disciplina")
        print("0 - Voltar ao menu principal")

        op = input("Escolha: ")

        # CRIAR
        if op == "1":
         nome = input("Nome da disciplina: ")
         sucesso, msg = criar_disciplina(user_id, nome)
         print(msg)

        # LISTAR
        elif op == "2":
            disciplinas = listar_disciplinas(user_id)

            if not disciplinas:
                print("Nenhuma disciplina cadastrada")
            else:
                for d in disciplinas:
                    print(f"{d[0]} - {d[1]}")


        # EDITAR
        elif op == "3":
            disciplinas = listar_disciplinas(user_id)

            if not disciplinas:
                print("Nenhuma disciplina para editar")
                continue

            for d in disciplinas:
                print(f"{d[0]} - {d[1]}")

            did = input("ID da disciplina: ")
            novo_nome = input("Novo nome: ")
            print(editar_disciplina(user_id, did, novo_nome)[1])

        # EXCLUIR
        elif op == "4":
            disciplinas = listar_disciplinas(user_id)

            if not disciplinas:
                print("Nenhuma disciplina para excluir")
                continue

            for d in disciplinas:
                print(f"{d[0]} - {d[1]}")

            did = input("ID da disciplina: ")
            sucesso, msg = excluir_disciplina(user_id, did)
            print(msg)

        elif op == "0":
            break