from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

inventario = {}
console = Console()

def adicionar_item(nome, quantidade=1, tipo=None, dano=0, cura=0, descricao=""):
    if nome in inventario:
        inventario[nome]["quantidade"] += quantidade
    else:
        inventario[nome] = {
            "quantidade": quantidade,
            "tipo": tipo,         # Ex: "arma", "consumível", "chave", etc.
            "dano": dano,         # Se for uma arma
            "cura": cura,         # Se for uma poção
            "descricao": descricao
        }
    console.print(f"[green]{quantidade}x {nome} adicionado(s) ao inventário.[/green]")

def remover_item(nome, quantidade=1):
    if nome in inventario:
        inventario[nome]["quantidade"] -= quantidade
        if inventario[nome]["quantidade"] <= 0:
            del inventario[nome]
        console.print(f"[red]{quantidade}x {nome} removido(s) do inventário.[/red]")
    else:
        console.print(f"[yellow]{nome} não está no inventário.[/yellow]")

def mostrar_inventario():
    if not inventario:
        console.print(Panel("[bold red]Seu inventário está vazio.[/bold red]", title="Inventário"))
        return

    tabela = Table(title="Inventário", header_style="bold cyan")
    tabela.add_column("Item", style="bold white")
    tabela.add_column("Qtd", justify="center")
    tabela.add_column("Tipo", justify="center")
    tabela.add_column("Dano", justify="center")
    tabela.add_column("Cura", justify="center")
    tabela.add_column("Descrição", style="dim")

    for nome, info in inventario.items():
        tabela.add_row(
            nome,
            str(info["quantidade"]),
            info["tipo"] or "-",
            str(info["dano"]) if info["dano"] else "-",
            str(info["cura"]) if info["cura"] else "-",
            info["descricao"] or "-"
        )

    painel = Panel(tabela, title="🧳 Inventário do Jogador", border_style="green")
    console.print(Align.center(painel))

