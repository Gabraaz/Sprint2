import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typedPrint(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def color_text(text, cor="branco"):
    cores = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "magenta": "\033[95m",
        "ciano": "\033[96m",
        "branco": "\033[97m",
        "reset": "\033[0m"
    }
    return f"{cores.get(cor, cores['branco'])}{text}{cores['reset']}"
