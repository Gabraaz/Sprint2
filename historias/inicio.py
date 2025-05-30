from InquirerPy import inquirer
from prompt_toolkit.styles import Style
from time import sleep
from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from util import typedPrint, Config, clear_screen
from personagem.inventario import adicionar_item, remover_item, mostrar_inventario
from historias.floresta import floresta_inicio

console = Console()

# Dicionário de estilo simples
style_dict = {
    "question": "bold",
    "answer": "italic",
    "pointer": "bold #00ffff",     # Ciano brilhante
    "selected": "#ff9d00",         # Laranja
    "separator": "#666666",
    "instruction": "",
    "text": "",
}

# Converte o dicionário para o objeto que o InquirerPy espera
style = Style.from_dict(style_dict)


def intro_jogo():
    clear_screen()
    
    # Painel de título com um estilo épico
    titulo = Text("🌑 PRÓLOGO 🌒", style="bold magenta on black", justify="center")
    console.print(Align.center(Panel(titulo, width=60, border_style="magenta")), justify="center")
    sleep(1)

    # Textos narrativos com delays para dar ritmo
    falas = [
        "Em um mundo distante do nosso, existe uma terra esquecida chamada [bold cyan]Virelia[/bold cyan].",
        "Por gerações, a vila de [bold white]LUNARIS[/bold white] viveu em paz... até o surgimento de [bold red]Griffin[/bold red].",
        "[bold red]Um mago poderoso e corrompido pela escuridão[/bold red], que lançou uma maldição sobre todos.",
        "Agora, as [bold yellow]colheitas apodrecem[/bold yellow], o céu [bold blue]chora cinzas[/bold blue], e os dias são devorados pela [bold grey37]névoa[/bold grey37].",
        "Você, um [italic]forasteiro de origem incerta[/italic], acorda na costa de [bold cyan]Virelia[/bold cyan] — ferido, confuso, mas vivo.",
        "[bold green]O destino lhe deu um papel: derrotar Griffin e libertar esta terra da sombra.[/bold green]"
    ]

    for fala in falas:
        console.print(Align.center(Text.from_markup(fala, justify="center")), justify="center")
        sleep(2)

    console.print(Align.center(Panel("[bold white]Pressione Enter para continuar...[/bold white]", style="dim")), justify="center")
    input()
    clear_screen()

    # Menu interativo com ponteiro
    
    opcao = inquirer.select(
        message="Você se ergue da areia fria. Três escolhas se desenham diante de você:",
        choices=[
            "🌊 Vasculhar a praia em busca de suprimentos",
            "🌲 Adentrar a floresta sombria à frente",
            "🕰️ Esperar por ajuda... se é que ela virá"
        ],
        pointer="➤",
        style=style_dict
    ).execute()

    if "praia" in opcao:
        explorar_praia()
    elif "floresta" in opcao:
        explorar_floresta()
    elif "Esperar" in opcao:
        console.print(Align.center(Text("Você espera... mas só o som das ondas responde. O tempo está contra você.", style="dim italic")))
        sleep(2)
        input("Pressione Enter para continuar...")
        explorar_inicio()

def transicao_para_floresta():
    console.clear()
    frases = [
        "Você deixa a brisa salgada da praia para trás...",
        "O som das ondas vai se tornando distante...",
        "O verde começa a dominar sua visão...",
        "A luz do sol enfraquece sob as copas das árvores...",
        "Você entrou na floresta."
    ]
    
    for frase in frases:
        console.print(Align.center(Text(frase, style="italic cyan")), justify="center")
        sleep(1.5)

    sleep(1)
    console.print(Align.center(Panel("🌲 [bold green]Floresta de Virelia[/bold green] 🌲", border_style="green")), justify="center")
    sleep(2)
    sleep(15)

def explorar_praia():
    clear_screen()
    typedPrint("Você caminha pela praia deserta. Conchas partidas e madeira quebrada contam histórias antigas.", Config.speed)
    typedPrint("Algo brilha sob o sol pálido. Você cava com as mãos... é um canivete enferrujado.", Config.speed)
    typedPrint("Não é muito, mas é o começo de uma resistência.", Config.speed)
    adicionar_item(
        "Canivete Enferrujado",
        quantidade=1,
        tipo="Arma Básica",
        dano=5,
        descricao="Um canivete velho, mas um pouco afiado."
    )

    mostrar_inventario()
    sleep(4)

    transicao_para_floresta()  # Aqui entra a mágica da transição
    explorar_floresta()

def explorar_floresta():
    clear_screen()
    typedPrint("A floresta de Virelia é densa e úmida. A luz quase não penetra pelas copas escuras.", Config.speed)
    typedPrint("Você sente olhos te observando... e um arrepio percorre sua espinha.", Config.speed)
    typedPrint("De repente, um ruído seco. Algo — ou alguém — se move entre os arbustos.", Config.speed)
    floresta_inicio()