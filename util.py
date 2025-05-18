# util.py
import os
import time

class Config:
    speed = 0.05

def clear_screen(): #funçao para limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def typedPrint(texto, delay=0.05): #funçao para fazer o texto animado.
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay if char not in ".!?,:" else delay + 0.1)
    print()





