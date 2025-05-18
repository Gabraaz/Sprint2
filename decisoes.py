# dentro do if escolha == "2":
from random import choice
from fofocas import fofocas_disponiveis
from caderno import anotar_missao


def decisao_fofoca()
    fofoca = choice(fofocas_disponiveis)
    typedPrint(f"Você ouve: \"{fofoca}\"", Config.speed)

    print("\nO que deseja fazer?")
    print("1. Explorar agora")
    print("2. Anotar no caderno para mais tarde")
    print("3. Ignorar")

    decisao = input("Escolha: ")

    if decisao == "1":
        typedPrint("Você decide investigar imediatamente!", Config.speed)
        # Aqui entra a lógica da missão
    elif decisao == "2":
        anotar_missao(fofoca)
    elif decisao == "3":
        print("Você decide que é só papo de bêbado e ignora.")
    else:
        print("Escolha inválida.")
