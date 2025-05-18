from util import clear_screen
from util import Config, typedPrint
from telas.taverna import taverna
from historias.inicio import intro_jogo

# Tela Menu
def menu_principal():
    while True:
        clear_screen()
        print("=== BEM-VINDO AO RPG DO VILLAREJO ===")
        print("1. Jogar")
        print("2. Ler Regras")
        print("3. Inserir Código Secreto")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            typedPrint("Iniciando o jogo...", Config.speed)
            intro_jogo() #temporario para testes.
            break  # por enquanto só sai do loop
        elif escolha == "2":
            clear_screen()
            print("\n📜 Regras do Jogo:")
            print("• Explore a floresta e derrote inimigos.")
            print("• Visite o vilarejo para comprar melhorias.")
            print("• Sobreviva e vença o desafio final!")
        elif escolha == "3":
            codigo = input("\nDigite seu código mágico: ")
            print(f"Código '{codigo}' recebido! (função bônus virá depois)")
        elif escolha == "4":
            print("Saindo do jogo... Até logo!")
            clear_screen()
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")
        print("\n" + "=" * 40 + "\n")
