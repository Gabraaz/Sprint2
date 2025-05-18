# caderno.py

caderno_de_missoes = []

def anotar_missao(missao):
    caderno_de_missoes.append(missao)
    print(f"Missão anotada no caderno: '{missao}'")

def listar_missoes():
    if not caderno_de_missoes:
        print("O caderno está vazio.")
    else:
        print("\n📖 Missões no caderno:")
        for i, missao in enumerate(caderno_de_missoes, 1):
            print(f"{i}. {missao}")
