from serv.estatisticas import *

def formatar(minutos):
    h = minutos // 60
    m = minutos % 60
    return f"{h}h {m}min"

def menu_estatisticas(user_id):
    while True:
        print("\n===== ESTATÍSTICAS =====")
        print("1 - Ver resumo geral")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            total = tempo_total(user_id)
            hoje = tempo_hoje(user_id)
            top = disciplina_top(user_id)
            streak = streak_estudo(user_id)
            por_disc = tempo_por_disciplina(user_id)

            print("\n📊 RESUMO")
            print("Tempo total:", formatar(total))
            print("Hoje:", formatar(hoje))
            print("Disciplina favorita:", top or "Nenhuma")
            print("Streak:", streak, "dias 🔥")

            print("\nTempo por disciplina:")
            for nome, tempo in por_disc:
                print(f"{nome}: {formatar(tempo)}")

            input("\nENTER para voltar")

        elif op == "0":
            break