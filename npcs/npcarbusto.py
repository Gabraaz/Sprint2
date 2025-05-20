from util import clear_screen, typedPrint, color_text

from InquirerPy import inquirer

# NPCarbusto.py

import random
import time
import os

def npc_brotando_do_arbusto():
    clear_screen()
    typedPrint("\n🌿 Você ouve um farfalhar estranho vindo de um arbusto...", 0.04)
    time.sleep(0.5)
    typedPrint("👀 Um estranho se levanta, tirando folhas do cabelo.", 0.04)
    time.sleep(1.5)

    NomeRealNpc = "Landir"
    NomeColorido = color_text(NomeRealNpc, "amarelo")
    Nome_visivel = "???"


    clear_screen()
    time.sleep(0.5)
    print("\n👤 ???:", end=" ")
    typedPrint("Olá meu jovem, desculpa te assustar... estava caçando coelhos", 0.04)
    time.sleep(1.5)
    typedPrint(f"👤 ???: Nunca te vi por aqui, veio da onde?", 0.04)

    while True:
        escolha = inquirer.select(
            message="Escolha uma opção:",
            choices=[
                "Quem é voce?",
                "Aonde estou?",
                "Atacar ele"
            ],
            pointer="👉",
        ).execute()
        if escolha == "Quem é voce?":
            typedPrint("QUem é voce...?...", 0.04)
            time.sleep(1)
            break
        elif escolha == "Aonde estou?":
            clear_screen()
        elif escolha == "Atacar ele":
            print("Ele te Matou")
        elif escolha == "Sair":
            print("Saindo do jogo... Até logo!")
            clear_screen()
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")
        print("\n" + "=" * 40 + "\n")








        # print("\n...?")
        # print("1. Quem é voce?")
        # print("2. Aonde estou?")
        # print("3. Atacar ele")

        # escolha = input("Escolha uma opção: ").strip()

        # if escolha == "1":
        #     print(f"\n👤 ???:", end=" ")
        #     typedPrint("Tá bom, tá bom... Meu nome é ", 0.04)

        #     nome_visivel = NomeColorido  # Muda só aqui, depois do "Meu nome é"
        #     print(f"👤 {nome_visivel}:", end=" ")
        #     typedPrint(" Landir.", 0.04)

        # elif escolha == "2":
        #     typedPrint(f"\n{NomeNpcArbusto}: Eu tô aqui estudando. Cada arbusto esconde um segredo, e cada segredo pode esconder uma espada. Ou um esquilo.", 0.04)
        # elif escolha == "3":
        #     typedPrint("\n🚶‍♂️ Você se afasta do arbusto, fingindo que nada aconteceu.", 0.04)
        #     break
        # else:
        #     typedPrint("❌ Opção inválida. Escolha 1, 2 ou 3.", 0.04)
        #     clear_screen()
