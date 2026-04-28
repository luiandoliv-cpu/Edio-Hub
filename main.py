from serv.sessao import carregar_sessao
from screens.startmenu import tela_inicial
from screens.menuprincip import menu_principal

def main():
    '''Roda o programa (de acordo com presença ou ausência de sessão)'''
    while True:
        user_id = carregar_sessao()

        if user_id:
            resultado = menu_principal(user_id)

            if resultado == "exit":
                break   

        else:
            resultado = tela_inicial()

            if resultado == "exit":
                break   

if __name__ == "__main__":
    main()