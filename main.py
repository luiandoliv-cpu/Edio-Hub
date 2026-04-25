# ================================
# MAIN.PY - PONTO DE ENTRADA
# ================================

from screens.startmenu import tela_inicial

def main():
   user_id = tela_inicial()

   if user_id:
        tela_inicial()
main()