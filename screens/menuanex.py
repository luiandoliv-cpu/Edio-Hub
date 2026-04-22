from serv.parede import *
from serv.utils import limpar_tela
import time

def menu_mural(user_id):
    while True:
        print("\n===== Lembretes =====")
        print("1 - Criar lembrete")
        print("2 - Acessar mural")
        print("3 - Excluir lembrete")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            sucesso, msg = criar_anexo(user_id)
            print(msg)

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

        elif op == "3":
            excluir_anexo(user_id)

        elif op == "0":
            limpar_tela()
            break

        else:
            print("Opção inválida.")
            time.sleep(2)
            limpar_tela()
