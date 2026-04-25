from serv.temporizadores import *
from serv.disciplinas import listar_disciplinas
from serv.utils import limpar_tela
import time

def menu_temporizadores(user_id):
    while True:
        limpar_tela()
        print("\n===== Temporizadores =====")
        print("1 - Criar temporizador")
        print("2 - Listar temporizadores")
        print("3 - Iniciar temporizador")
        print("4 - Editar temporizador")
        print("5 - Excluir temporizador")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            limpar_tela()
            print("=== Criar temporizador ===")

            disciplinas = listar_disciplinas(user_id)

            if not disciplinas:
                print("Você precisa criar uma disciplina primeiro.")
                input("\nPressione ENTER para voltar...")
                limpar_tela()
                continue

            print("\nEscolha a disciplina:")
            for d in disciplinas:
                print(f"{d[0]} - {d[1]}")

            try:
              discip_id = int(input("ID da disciplina: "))
            except ValueError:
                print("ID inválido.")
                input("\nPressione ENTER...")
                limpar_tela()
                continue

            nome = input("Nome: ")

            try:
                estudo = int(input("Tempo estudo (min): "))
            except ValueError:
                print("Tempo inválido.")
                input("\nPressione ENTER...")
                limpar_tela()
                continue

            pausa = input("Tempo pausa (min ou vazio): ").strip()
            pausa = int(pausa) if pausa else 0

            print(criar_temporizador(user_id, nome, discip_id, estudo, pausa)[1])
            input("\nPressione ENTER para voltar...")
            limpar_tela()

        elif op == "2":
            timers = listar_temporizadores(user_id)
            for t in timers:
                print(f"{t[0]} - {t[1]} | estudo:{t[2]}min pausa:{t[3]}min")
            input("\nPressione ENTER para voltar...")
            limpar_tela()

        elif op == "3":
            limpar_tela()
            tid = input("ID do temporizador: ")
            limpar_tela()
            print(iniciar_temporizador(user_id, tid)[1])
            input("\nPressione ENTER...")
            limpar_tela()

        elif op == "4":
            limpar_tela()
            tid = input("ID: ")
            limpar_tela()
            estudo = input("Novo tempo estudo: ")
            pausa = input("Nova pausa: ")
            print(editar_temporizador(user_id, tid, estudo, pausa)[1])
            input("\nPressione ENTER...")
            limpar_tela()

        elif op == "5":
            limpar_tela()
            tid = input("ID: ")
            limpar_tela()
            print(excluir_temporizador(user_id, tid)[1])
            input("\nPressione ENTER...")
            limpar_tela()

        elif op == "0":
            limpar_tela()
            break

        else:
            print("Opção inválida.")
            time.sleep(2)
            limpar_tela()