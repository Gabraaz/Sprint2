# intro.py
from util import typedPrint, Config, clear_screen
from personagem.inventario import adicionar_item, remover_item, mostrar_inventario
from historias.floresta import floresta_inicio

def intro_jogo():
    clear_screen()
    print("\n=== PRÓLOGO ===\n")
    typedPrint("O balanço do mar ainda ecoa na sua cabeça.", Config.speed)
    typedPrint("Você acorda numa praia estranha, com a memória feita em pedaços.", Config.speed)
    typedPrint("Não de onde veio. Não sabe por que estava no mar.", Config.speed)
    typedPrint("Mas sabe de uma coisa: está vivo. E isso é um começo.", Config.speed)
    input("\nPressione Enter para continuar...")
    clear_screen()
    print("\nVocê se levanta da areia, ainda zonzo. Três caminhos se apresentam:")
    print("1. Explorar a praia")
    print("2. Entrar na floresta próxima")
    print("3. Ficar esperando... talvez a ajuda venha")

    escolha = input("O que deseja fazer? ")

    if escolha == "1":
        explorar_praia()
    elif escolha == "2":
        explorar_floresta()
    elif escolha == "3":
        print("Você espera... mas ninguém vem. O sol castiga. Melhor se mover.")
        input("Pressione Enter para continuar...")
        explorar_inicio()
    else:
        print("Escolha inválida.")
        input("Pressione Enter para tentar de novo...")
        explorar_inicio()

def explorar_praia():
    clear_screen()
    typedPrint("Você caminha pela praia. Conchas, destroços de um barco... algo brilha na areia.", Config.speed)
    typedPrint("Você encontra um canivete enferrujado. Não é muito, mas pode ser útil.", Config.speed)
    adicionar_item("Canivete Enferrujado", quantidade=1, tipo="Arma Basica", dano=5, descricao="Um canivete velho, mas um pouco afiado.")
    mostrar_inventario()
    explorar_floresta()  # Leva pra floresta depois

def explorar_floresta():
    clear_screen()
    typedPrint("A floresta é densa. Sons estranhos ecoam entre as árvores.", Config.speed)
    typedPrint("Você sente que está sendo observado.", Config.speed)
    typedPrint("Barulhos vem de um arbusto perto de vocë..", Config.speed)
    floresta_inicio() 