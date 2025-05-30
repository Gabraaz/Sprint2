from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from util import typedPrint, Config, clear_screen
from personagem.inventario import adicionar_item, mostrar_inventario

import time

console = Console()

def encontrar_eloria():
    clear_screen()
    typedPrint("A floresta se torna cada vez mais silenciosa.", Config.speed)
    typedPrint("Folhas sussurram segredos antigos... Você sente que está sendo observado.", Config.speed)
    typedPrint("De repente, uma árvore solitária surge em uma clareira, com um amuleto pendurado em um dos galhos.", Config.speed)

    input("\n[Pressione Enter para tocar o amuleto...]")
    clear_screen()

    typedPrint("Ao tocar o amuleto, a floresta inteira parece prender a respiração.", Config.speed)
    typedPrint("Uma onda de energia varre tudo ao redor. A névoa se abre.", Config.speed)

    painel_descoberta = Panel(
        Align.center("[bold cyan]Você descobriu a vila escondida de Eloria[/bold cyan]", vertical="middle"),
        title="[green]Descoberta[/green]",
        subtitle="Um novo capítulo começa",
        width=60,
        style="bold green"
    )
    console.print(painel_descoberta)

    typedPrint("\nA vila repousa num vale oculto, protegida por magia antiga.", Config.speed)
    typedPrint("Pessoas observam você com surpresa. Uma senhora se aproxima, com olhos cansados, mas atentos.", Config.speed)

    painel_dialogo = Panel(
        Align.center('"Você... saiu da floresta? O Guardião escolheu você."', vertical="middle"),
        title="[magenta]Anciã Misteriosa[/magenta]",
        width=60,
        style="dim"
    )
    console.print(painel_dialogo)

    typedPrint("Ela toca seu peito, onde agora repousa o [Amuleto do Guardião].", Config.speed)

    adicionar_item(
        "Amuleto do Guardião",
        quantidade=1,
        tipo="Item Especial",
        dano=0,
        descricao="Um artefato antigo que vibra com energia protetora."
    )

    mostrar_inventario()
    time.sleep(3)

    typedPrint("\nVocê sente que sua jornada em Virelia está apenas começando...", Config.speed)
    input("\n[Pressione Enter para continuar...]")
