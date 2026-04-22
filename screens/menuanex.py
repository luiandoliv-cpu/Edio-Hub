from serv.parede import criar_anexo, listar_anexos, excluir_anexo
from serv.utils import limpar_tela
import time

def menu_mural(user_id):
    while True:
        limpar_tela()
        print("\n===== Lembretes =====")
        print("1 - Criar lembrete")
        print("2 - Acessar mural")
        print("3 - Excluir lembrete")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            limpar_tela()
            sucesso, msg = criar_anexo(user_id)
            print(msg)
            limpar_tela()

        elif op == "2":
            limpar_tela()
            anexos = listar_anexos(user_id)

            if not anexos:
                print("Mural vazio.")
            else:
                print("\n                   --- SEUS LEMBRETES ---")
                for a in anexos:
                    print(f"""
                ID: {a[0]}
                Título: {a[1]}
                Mensagem: {a[2]}
                    ---------------------""")
            input("\nPressione ENTER para voltar...")
            limpar_tela()   
   
        elif op == "3":
            limpar_tela()
            excluir_anexo(user_id)
            limpar_tela()

        elif op == "0":
            limpar_tela()
            break

        else:
            print("Opção inválida.")
            time.sleep(2)
            limpar_tela()
