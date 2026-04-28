import os
import time

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausa_auto(msg, segundos=2):
    limpar_tela()
    print(f"\n{msg}")
    time.sleep(segundos)
    limpar_tela()