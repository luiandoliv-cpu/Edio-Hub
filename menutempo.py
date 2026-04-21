from temporizadores import *

def menu_temporizadores(user_id):
    while True:
        print("\n===== TEMPORIZADORES =====")
        print("1 - Criar temporizador")
        print("2 - Listar temporizadores")
        print("3 - Iniciar temporizador")
        print("4 - Editar temporizador")
        print("5 - Excluir temporizador")
        print("6 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            estudo = input("Tempo estudo (min): ")
            pausa = input("Tempo pausa (min ou vazio): ")
            print(criar_temporizador(user_id, nome, estudo, pausa)[1])

        elif op == "2":
            timers = listar_temporizadores(user_id)
            for t in timers:
                print(f"{t[0]} - {t[1]} | estudo:{t[2]}min pausa:{t[3]}min")

        elif op == "3":
            tid = input("ID do temporizador: ")
            print(iniciar_temporizador(user_id, tid)[1])

        elif op == "4":
            tid = input("ID: ")
            estudo = input("Novo tempo estudo: ")
            pausa = input("Nova pausa: ")
            print(editar_temporizador(user_id, tid, estudo, pausa)[1])

        elif op == "5":
            tid = input("ID: ")
            print(excluir_temporizador(user_id, tid)[1])

        elif op == "6":
            break