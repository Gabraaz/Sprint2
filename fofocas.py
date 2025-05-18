import random
import time
from util import Config, typedPrint

fofocas_disponiveis = [
    "Ouvi dizer que um dragão antigo foi visto perto das colinas geladas.",
    "Dizem que um ladrão escondeu um tesouro no poço atrás da igreja.",
    "Uma aldeã jura ter visto luzes estranhas na floresta à noite.",
    "Há quem diga que o cemitério abriga mais que apenas mortos.",
    "O velho taverneiro já foi um guerreiro lendário... ou assim ele diz.",
]

fofocas_ouvidas = []
caderno_de_missoes = []


def fofoca_aleatoria():
    if not fofocas_disponiveis:
        return None  # Nenhuma fofoca nova
    fofoca = random.choice(fofocas_disponiveis)
    fofocas_disponiveis.remove(fofoca)
    fofocas_ouvidas.append(fofoca)
    return fofoca

caderno_de_missoes = []

def anotar_missao(missao):
    caderno_de_missoes.append(missao)
    typedPrint("Missão anotada no caderno. Você pode investigá-la mais tarde.", Config.speed)

def mostrar_caderno():
    if not caderno_de_missoes:
        print("Seu caderno está vazio.")
    else:
        print("\n=== CADERNO DE MISSÕES ===")
        for i, missao in enumerate(caderno_de_missoes, start=1):
            print(f"{i}. {missao}")

def decisao_fofoca(fofoca):
    typedPrint(f"\nVocê ouve: \"{fofoca}\"", Config.speed)
    time.sleep(1)

    print("\nO que deseja fazer?")
    print("1. Explorar agora")
    print("2. Anotar no caderno para mais tarde")
    print("3. Ignorar")

    decisao = input("Escolha: ")

    if decisao == "1":
        typedPrint("Você decide investigar imediatamente!", Config.speed)
        # Aqui entra a lógica da missão no ato
    elif decisao == "2":
        anotar_missao(fofoca)
    elif decisao == "3":
        print("Você decide que é só papo de bêbado e ignora.")
    else:
        print("Escolha inválida.")
