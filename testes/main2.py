from util2 import typedPrint, clear_screen, color_text
from rich_test import exibir_logo  # ou de onde estiver sua função
import pyfiglet
import time
import os




def mostrar_logo():
    try:
        with open("assets/logo.txt", "r", encoding="utf-8") as file:
            print(pyfiglet.figlet_format("Bem - Vindo"))
    except FileNotFoundError:
        print(color_text("[Logo não encontrada - crie assets/logo.txt]", "vermelho"))

def menu():
    while True:
        clear_screen()
        mostrar_logo()
        typedPrint(color_text("\n🎮 Bem-vindo ao Terminal Estiloso!\n", "amarelo"), 0.03)
        time.sleep(0.8)
        print(color_text("1. Iniciar Jogo", "verde"))
        print(color_text("2. Configurações", "amarelo"))
        print(color_text("3. Sair", "vermelho"))

        escolha = input(color_text("\nEscolha uma opção: ", "branco")).strip()

        if escolha == "1":
            typedPrint(color_text("\n🧙 Carregando o jogo...", "ciano"), 0.04)
            time.sleep(1.5)
        elif escolha == "2":
            typedPrint(color_text("\n⚙️ Abriu as configurações... (ainda em construção)", "amarelo"), 0.04)
            time.sleep(1.5)
        elif escolha == "3":
            typedPrint(color_text("\n👋 Saindo... até logo!", "vermelho"), 0.04)
            break
        else:
            typedPrint(color_text("\n❌ Opção inválida. Tente de novo.", "vermelho"), 0.04)
            time.sleep(1.2)

if __name__ == "__main__":
    menu()
