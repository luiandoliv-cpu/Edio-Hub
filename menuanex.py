from parede import criar_anexo, listar_anexos, excluir_anexo

def menu_mural(user_id):
    while True:
        print("\n===== MURAL DE LEMBRETES =====")
        print("1 - Criar lembrete")
        print("2 - Acessar mural")
        print("3 - Excluir lembrete")
        print("4 - Voltar")

        op = input("Escolha: ")

        # CRIAR
        if op == "1":
            sucesso, msg = criar_anexo(user_id)
            print(msg)

        # LISTAR / ACESSAR
        elif op == "2":
            anexos = listar_anexos(user_id)

            if not anexos:
                print("Mural vazio.")
            else:
                print("\n--- SEUS LEMBRETES ---")
                for a in anexos:
                    print(f"""
ID: {a[0]}
Título: {a[1]}
Mensagem: {a[2]}
---------------------""")

        # EXCLUIR
        elif op == "3":
            excluir_anexo(user_id)

        # VOLTAR
        elif op == "4":
            break

        else:
            print("Opção inválida.")