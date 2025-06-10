# util.py
import os
import time
import shutil


class Config:
    speed = 0.05


# APAGAR TERMINAL
def clear_screen(): #funçao para limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# ANIMAR TEXTO

def typedPrint(texto, delay=0.05):
    texto = str(texto)  # Garante que 'texto' é uma string
    for char in texto:
        if char in ".!?,:":
            time.sleep(delay + 0.1)
        else:
            time.sleep(delay)
        print(char, end='', flush=True)
    print()

# COR PARA TEXTO
def color_text(text, cor="amarelo"):
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



#CENTRALIZAR TEXTO
def centralizar_com_ponteiro(texto):
    largura_terminal = shutil.get_terminal_size().columns
    largura_texto = len(texto)
    largura_total = largura_texto + 4  # 4 = espaço pro ponteiro ➤ e espaço extra
    margem = max((largura_terminal - largura_total) // 2, 0)
    return " " * margem + texto

