from serv.temporizadores import *
from serv.utils import limpar_tela

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
            nome = input("Nome: ")
            estudo = input("Tempo estudo (min): ")
            pausa = input("Tempo pausa (min ou vazio): ")
            print(criar_temporizador(user_id, nome, estudo, pausa)[1])

        elif op == "2":
            timers = listar_temporizadores(user_id)
            for t in timers:
                print(f"{t[0]} - {t[1]} | estudo:{t[2]}min pausa:{t[3]}min")
                time.sleep(8)

        elif op == "3":
            limpar_tela()
            tid = input("ID do temporizador: ")
            limpar_tela()
            print(iniciar_temporizador(user_id, tid)[1])

        elif op == "4":
            limpar_tela()
            tid = input("ID: ")
            limpar_tela()
            estudo = input("Novo tempo estudo: ")
            pausa = input("Nova pausa: ")
            print(editar_temporizador(user_id, tid, estudo, pausa)[1])

        elif op == "5":
            limpar_tela()
            tid = input("ID: ")
            limpar_tela()
            print(excluir_temporizador(user_id, tid)[1])

        elif op == "0":
            limpar_tela()
            break

        else:
            print("Opção inválida.")
            time.sleep(2)
            limpar_tela()
