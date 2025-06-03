from util import Config, typedPrint, clear_screen
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from rich.progress import Progress
from rich.style import Style
from rich.box import ROUNDED, HEAVY
from InquirerPy import inquirer, get_style
from playsound import playsound
from codigos import tela_resgate_codigo
from historias.inicio import intro_jogo
from historias.floresta import floresta_inicio
import time

console = Console()

# Estilo personalizado para o menu
def get_menu_style():
    return {
        "questionmark": "#FFD700 bold",
        "answer": "#7FFF00 bold",
        "input": "#FFFFFF",
        "question": "bold",
        "pointer": "#7B03FC bold",
        "highlighted": "#FF4500",
        "selected": "#7FFF00",
        "separator": "#555555",
        "instruction": "#AAAAAA"
    }

def tela_carregamento(mensagem="Carregando Jogo", jogador=None):
    """Barra de carregamento estilizada com Rich"""
    clear_screen()
    
    # Garante que a mensagem seja string
    if not isinstance(mensagem, str):
        mensagem = str(mensagem)

    console.print(
        Panel.fit(
            Text(mensagem, justify="center", style="bold cyan"),
            border_style="cyan",
            box=HEAVY,
            padding=(1, 10)
        ),
        justify="center"
    )
    
    with Progress(transient=True) as progress:
        task = progress.add_task("[cyan]Carregando...", total=100)
        while not progress.finished:
            progress.update(task, advance=3)
            time.sleep(0.03)

    console.print(
        Panel.fit(
            Text("✓ PRONTO!", style="bold green"),
            border_style="green",
            padding=(1, 8)
        ),
        justify="center"
    )
    
    time.sleep(0.8)
    menu_principal(jogador)

def menu_principal(jogador):
    while True:
        clear_screen()

        # Logo em destaque
        titulo = Panel.fit(
            Text("🌟 VIRELIA 🌟", justify="center", style="bold magenta"),
            border_style="bright_magenta",
            box=ROUNDED,
            padding=(1, 10)
        )

        subtitulo = Text("USE AS SETAS ↑ ↓ E ENTER PARA SELECIONAR", justify="center", style="bold italic cyan")
        instrucoes = Panel.fit(subtitulo, box=ROUNDED, border_style="dim")

        console.print(Columns([titulo], align="center"), justify="center")
        console.print(Columns([instrucoes], align="center"), justify="center")
        console.print("\n")

        # Menu com opções
        escolha = inquirer.select(
            qmark="",
            message="Escolha uma opção:",
            choices=[
                "🎮  Jogar",
                "📖  Ler Regras",
                "🔑  Resgatar Código",
                "🚪  Sair"
            ],
            pointer="➤",
            style=get_style(get_menu_style())
        ).execute()

        # Ações de cada escolha
        if escolha == "🎮  Jogar":
            with console.status("[bold green]Iniciando aventura...", spinner="dots"):
                playsound("sons/iniciandojogo.mp3")
                time.sleep(2)
            floresta_inicio()   #USADO PARA PUXAR FUNCOES E TESTES
            break

        elif escolha == "📖  Ler Regras":
            playsound("sons/entrartela.mp3")
            clear_screen()
            regras = "\n".join([
                "• 🌲 Explore a floresta e descubra segredos ocultos.",
                "• ⚔️ Derrote inimigos e colete recursos.",
                "• 🏡 Visite a taverna para recuperar energias.",
                "• 🧙 Enfrente o mago sombrio no desafio final!"
            ])
            painel_regras = Panel.fit(
                Text(f"📜  REGRAS DO JOGO\n\n{regras}", justify="center", style="bold white"),
                border_style="blue",
                box=HEAVY,
                padding=(1, 8)
            )
            console.print(painel_regras, justify="center")
            time.sleep(1)

        elif escolha == "🔑  Resgatar Código":
            with console.status("[yellow]Carregando sistema de códigos...", spinner="moon"):
                time.sleep(1)
            tela_resgate_codigo(jogador)

        elif escolha == "🚪  Sair":
            playsound("sons/voltartela.mp3")
            console.print(
                Panel.fit(
                    Text("👋 Até a próxima aventura!", justify="center", style="italic bright_red"),
                    border_style="red",
                    box=ROUNDED,
                    padding=(1, 10)
                ),
                justify="center"
            )
            time.sleep(1.5)
            clear_screen()
            break

        input("\n[dim]Pressione Enter para continuar...")

