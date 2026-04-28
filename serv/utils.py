import os
import time

def limpar_tela():
    '''Limpa a tela'''
    os.system("cls" if os.name == "nt" else "clear")

def pausa_auto(msg, segundos=2):
    '''Pausa de tempo'''
    limpar_tela()
    print(f"\n{msg}")
    time.sleep(segundos)
    limpar_tela()

def vermelho(txt):
    '''Cor vermelha'''
    return f"\033[31m{txt}\033[0m"

def verde(txt):
    '''Cor verde'''
    return f"\033[32m{txt}\033[0m"

def amarelo(txt):
    '''Cor amarela'''
    return f"\033[33m{txt}\033[0m"

def azul(txt):
    '''Cor azul'''
    return f"\033[34m{txt}\033[0m"

def ciano(txt):
    '''Cor ciano'''
    return f"\033[36m{txt}\033[0m"