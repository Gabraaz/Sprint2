from rich import print
from rich.panel import Panel
import pyfiglet

def exibir_logo():
    ascii_logo = pyfiglet.figlet_format("Bem Vindo")
    print(f"[bold bright_white]{ascii_logo}[/bold bright_white]")
    print(Panel("[red]Use as setas ↑ ↓ e Enter para selecionar[/red]", expand=False))
    print("\n" + "=" * 40 + "\n")

