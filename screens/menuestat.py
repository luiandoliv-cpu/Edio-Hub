from serv.estatisticas import *
from serv.utils import *

def formatar(minutos):
    h = minutos // 60
    m = minutos % 60
    return f"{h}h {m}min"

def menu_estatisticas(user_id):
    '''Define a tela do menu de estatísticas do usuário'''
    while True:
        limpar_tela()
        print(ciano("\n===== ESTATÍSTICAS ====="))
        print("1 - Ver resumo geral")
        print(vermelho("0 - Voltar"))

        op = input("Escolha: ")

        if op == "1":
            limpar_tela()
            total = tempo_total(user_id)
            hoje = tempo_hoje(user_id)
            streak = streak_estudo(user_id)
            por_disc = tempo_por_disciplina(user_id)
            ranking = top_3_disciplinas(user_id)

            print("\n📊 RESUMO")
            print("Tempo total:", formatar(total))
            print("Hoje:", formatar(hoje))
            print("Streak:", streak, "dias 🔥")

            print("\nTempo por disciplina:")
            for nome, tempo in por_disc:
                print(f"{nome}: {formatar(tempo)}")

            print("\nDisciplinas mais estudadas:")
            if not ranking:
                print("Nenhuma disciplina registrada ainda.")
            else:
                posicoes = ["🥇", "🥈", "🥉"]
                for i, (nome, tempo) in enumerate(ranking):
                    print(f"{posicoes[i]} {nome} — {formatar(tempo)}")

            input("\nENTER para voltar")
            limpar_tela()
        elif op == "0":
            limpar_tela()
            break