from util import clear_screen
from util import Config, typedPrint
from telas.taverna import taverna
from historias.inicio import intro_jogo
from historias.floresta import floresta_inicio
from codigos import tela_resgate_codigo
from npcs.npcarbusto import npc_brotando_do_arbusto
from telas.telasrich import exibir_logo
from InquirerPy import inquirer
from playsound import playsound
from tqdm import tqdm



import time

# Tela Menu
from InquirerPy import inquirer
import time


def tela_carregamento(mensagem="Carregando Jogo", jogador=None):
    clear_screen()
    for _ in tqdm(range(30), desc=mensagem, ncols=60, bar_format="{l_bar}{bar}|"):
        time.sleep(0.05)
    time.sleep(1)
    if jogador is None: # tirar o not funciona, se ficar, nao funciona
        menu_principal(jogador)


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
            playsound("sons/iniciandojogo.mp3")
            typedPrint("Iniciando o jogo...", Config.speed)
            time.sleep(1)
            intro_jogo()  # temporário para testes
            break
        elif escolha == "Ler Regras":
            playsound("sons/entrartela.mp3")
            clear_screen()
            print("\n📜 Regras do Jogo:")
            print("• Explore a floresta e derrote inimigos.")
            print("• Visite o vilarejo para comprar melhorias.")
            print("• Sobreviva e vença o desafio final!")
        elif escolha == "Resgatar Código":
            tela_resgate_codigo(jogador)
        elif escolha == "Sair":
            playsound("sons/voltartela.mp3")
            print("Saindo do jogo... Até logo!")
            clear_screen()
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")
        print("\n" + "=" * 40 + "\n")
