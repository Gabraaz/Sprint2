#             ~~𝓘𝓜𝓟𝓞𝓡𝓣𝓢~~
from util import clear_screen
from util import Config, typedPrint
from moedas import mostrar_saldo, gastar
from fofocas import decisao_fofoca, mostrar_caderno, fofoca_aleatoria



def taverna():
    while True:
        clear_screen()
        print("\n=== TAVERNA DO VILLAREJO ===")
        print(f"Você tem {mostrar_saldo()} moedas.")
        print("1. Beber uma caneca de cerveja (5 moedas)")
        print("2. Ouvir as fofocas locais")
        print("3. Procurar por missões")
        print("4. Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            if gastar(5):
                typedPrint("Você bebeu uma caneca de cerveja e se sente revigorado!", Config.speed)
            else:
                print("Você não tem moedas suficientes para comprar o hidromel!")
            input("Pressione Enter para continuar...")
            clear_screen()

        elif escolha == "2":
            fofoca = fofoca_aleatoria()
            if fofoca:
                decisao_fofoca(fofoca)
            else:
                typedPrint("Sem conversas na taverna... volte mais tarde.", Config.speed)
                time.sleep(1)

        elif escolha == "3":
            typedPrint("Um velho aventureiro te propõe uma missão secreta!", Config.speed)
            # Aqui pode dar recompensas depois da missão
            recompensa = 10
            print(f"Você ganhou {recompensa} moedas pela missão!")
            input("Pressione Enter para continuar...")

        elif escolha == "4":
            print("Voltando ao menu principal...")
            clear_screen()
            break
        elif escolha == "5":
            typedPrint("Abrindo caderno...", Config.speed)
            clear_screen()
            mostrar_caderno()
            input("\nPressione Enter para voltar à taverna...")
            clear_screen()
        else:
            print("Opção inválida, tente novamente.")
            input("Pressione Enter para continuar...")