from rich import print
import pyfiglet

def exibir_logo():
    ascii_logo = pyfiglet.figlet_format("Bem Vindo")
    print(f"[bold bright_white]{ascii_logo}[/bold bright_white]")
    print("[red]Use as setas ↑ ↓ e Enter para selecionar[/red]")
    print("\n" + "=" * 40 + "\n")

