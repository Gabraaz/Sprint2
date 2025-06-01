from util import Config, typedPrint, clear_screen
from personagem.inventario import adicionar_item, remover_item, mostrar_inventario
from telas.taverna import taverna

import time

# Importa mostrar_caderno se usar ele aqui
# from fofocas import mostrar_caderno  # se existir

def floresta_inicio():

    while True:
        clear_screen()
        print("\nO que você vai fazer?")
        print("1. Ir até o arbusto")
        print("2. Continuar andando")
        print("3. Abrir o inventário")
        print("4. Abrir caderno")  # só se fizer sentido no contexto

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            typedPrint("Você vai devagar andando até o arbusto..", Config.speed)
            # Adicione aqui o que deve acontecer ao ir até o arbusto

        elif escolha == "2":
            typedPrint("Você continua andando pela floresta.", Config.speed)
            # Adicione aqui o que deve acontecer ao continuar andando

        elif escolha == "3":
            mostrar_inventario()
        elif escolha == "4":
            typedPrint("Abrindo caderno...", Config.speed)
            input("Pressione Enter para continuar...")
            clear_screen()
            # mostrar_caderno()  # Descomente se função existir
            input("\nPressione Enter para voltar...")
            clear_screen()

        else:
            print("Opção inválida, tente novamente.")
            input("Pressione Enter para continuar...")
