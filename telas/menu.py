from util import clear_screen
from util import Config, typedPrint
from telas.taverna import taverna
from historias.inicio import intro_jogo
from codigos import tela_resgate_codigo
from npcs.npcarbusto import npc_brotando_do_arbusto
from telas.telasrich import exibir_logo
from InquirerPy import inquirer

import time

# Tela Menu
from InquirerPy import inquirer
import time

def menu_principal(jogador):
    while True:
        clear_screen()
        exibir_logo()
        
        escolha = inquirer.select(
            message="Escolha uma opção:",
            choices=[
                "Jogar",
                "Ler Regras",
                "Resgatar Código",
                "Sair"
            ],
            pointer="👉",
        ).execute()

        if escolha == "Jogar":
            typedPrint("Iniciando o jogo...", Config.speed)
            time.sleep(1)
            npc_brotando_do_arbusto()  # temporário para testes
            break
        elif escolha == "Ler Regras":
            clear_screen()
            print("\n📜 Regras do Jogo:")
            print("• Explore a floresta e derrote inimigos.")
            print("• Visite o vilarejo para comprar melhorias.")
            print("• Sobreviva e vença o desafio final!")
        elif escolha == "Resgatar Código":
            tela_resgate_codigo(jogador)
        elif escolha == "Sair":
            print("Saindo do jogo... Até logo!")
            clear_screen()
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")
        print("\n" + "=" * 40 + "\n")
