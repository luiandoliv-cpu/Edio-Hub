import os
import time

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausa_auto(msg, segundos=2):
    limpar_tela()
    print(f"\n{msg}")
    time.sleep(segundos)
    limpar_tela()

def vermelho(txt):
    return f"\033[31m{txt}\033[0m"

def verde(txt):
    return f"\033[32m{txt}\033[0m"

def amarelo(txt):
    return f"\033[33m{txt}\033[0m"

def azul(txt):
    return f"\033[34m{txt}\033[0m"

def ciano(txt):
    return f"\033[36m{txt}\033[0m"