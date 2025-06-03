from util import Config, typedPrint, clear_screen
from player.inventario import adicionar_item, remover_item, mostrar_inventario
from assets.npc_scripts.salazar import primeiraFala_salazar
from telas.taverna import taverna
from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.text import Text
import time

# Importa mostrar_caderno se usar ele aqui
# from fofocas import mostrar_caderno  # se existir

console = Console()

def floresta_inicio():
    
    while True:
        clear_screen()
        console.print(Align.center(Panel("🌲 [bold green]Floresta de Virelia[/bold green] 🌲", border_style="green")), justify="center")
        print("\nO que você vai fazer?")
        print("1. Ir até o arbusto")
        print("2. Continuar andando")
        print("3. Abrir o inventário")
        print("4. Abrir caderno")  # só se fizer sentido no contexto

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            typedPrint("Você vai devagar andando até o arbusto...", Config.speed)
            
            # Inicia o papo com o Salazar
            while True:
                fala = input("Você: ")
                resposta = primeiraFala_salazar(fala)
                typedPrint(resposta, Config.speed)

                # Sai do loop se o diálogo chegou ao fim
                if "taverna" in resposta.lower() or "caminho" in resposta.lower():
                    break

        elif escolha == "2":
            typedPrint("Você continua andando pela floresta.", Config.speed)
            # Adicione aqui o que deve acontecer ao continuar andando

        elif escolha == "3":
            mostrar_inventario()
            input("Pressione Enter para continuar...")
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
